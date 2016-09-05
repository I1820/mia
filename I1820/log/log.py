# In The Name Of God
# ========================================
# [] File Name : log.py
#
# [] Creation Date : 04-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import datetime
try:
    from influxdb import InfluxDBClient
except ImportError:
    print("InfluxDB was not found, fall back to memory based storage")

from ..conf.config import cfg


class I1820Logger:
    _client = None

    @classmethod
    def _get_influx_client(cls) -> InfluxDBClient:
        if cls._client is None:
            cls._client = InfluxDBClient(host=cfg.influxdb_host,
                                         port=cfg.influxdb_port,
                                         username=cfg.influxdb_user,
                                         password=cfg.influxdb_passwd,
                                         database=cfg.influxdb_db)
        return cls._client

    def __init__(self, timestamp: datetime.datetime,
                 data: dict, endpoint: str):
        self.states = data['states']
        self.timestamp = timestamp
        self.endpoint = endpoint

    def save(self):
        points = []
        for key, value in self.states.items():
            point = {
                "measurement": key,
                "time": int(self.timestamp.timestamp()),
                "fields": {
                    "value": value
                }
            }
            points.append(point)
        self._get_influx_client().write_points(points)

    @classmethod
    def last(cls, measurement):
        results = cls._get_influx_client.query(
            'SELECT * FROM %s ORDER BY time DESC LIMIT 1' % measurement)
        print(results)
