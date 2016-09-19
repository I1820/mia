# In The Name Of God
# ========================================
# [] File Name : log.py
#
# [] Creation Date : 04-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .base import I1820Controller
try:
    from influxdb import InfluxDBClient
except ImportError:
    print("InfluxDB was not found, fall back to memory based storage")

from ..conf.config import cfg


class LogController(I1820Controller):

    def __init__(self):
        self._client = InfluxDBClient(host=cfg.influxdb_host,
                                      port=cfg.influxdb_port,
                                      username=cfg.influxdb_user,
                                      password=cfg.influxdb_passwd,
                                      database=cfg.influxdb_db)

    def save(self, measurement, type, rpi_id, device_id, time, value):
        points = [{
            "measurement": measurement,
            "tags": {
                "type": type,
                "rpi_id": rpi_id,
                "device_id": device_id
            },
            "time": time.strftime('%Y-%m-%dT%H:%M:%SZ'),
            "fields": {
                "value": value
            }
        }]
        self._client.write_points(points, time_precision="s")

    def last(self, measurement, rpi_id, device_id):
        q = ('SELECT * FROM %s'
             ' WHERE "rpi_id" = \'%s\' AND "device_id" = \'%s\''
             ' ORDER BY time DESC LIMIT 1;') % (measurement, rpi_id, device_id)
        results = self._client.query(q)
        last = next(results.get_points())
        return last['value']
