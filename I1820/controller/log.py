# In The Name Of God
# ========================================
# [] File Name : log.py
#
# [] Creation Date : 04-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .base import I1820Controller
from ..domain.log import I1820Log
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

    def save(self, log: I1820Log):
        points = []
        for key, value in log.states.items():
            point = {
                "measurement": key,
                "tags": {
                    "type": log.type,
                    "rpi_id": log.endpoint,
                    "device_id": log.device
                },
                "time": int(log.timestamp.timestamp()),
                "fields": {
                    "value": value
                }
            }
            points.append(point)
            self._client.write_points(points)

    def last(self, measurement, rpi_id, device_id):
        q = ('SELECT * FROM %s'
             ' WHERE "rpi_id" = \'%s\' AND "device_id" = \'%s\''
             ' ORDER BY time DESC LIMIT 1;') % (measurement, rpi_id, device_id)
        results = self._client.query(q)
        last = next(results.get_points())
        return last['value']
