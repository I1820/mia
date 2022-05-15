import pymongo

from ..conf.config import Config
from .base import LogAppender


class MongodbLogAppender(LogAppender):
    def __init__(self, cfg: Config):
        self._client = pymongo.MongoClient(host=cfg.appenders_mongodb_host,
                                           port=int(cfg.appenders_mongodb_port)
                                           )
        self._client = self._client[cfg.appenders_mongodb_db]

    def create(self, measurement, agent_id, device_id, time, value):
        collection = self._client[measurement]
        point = {
            "agent_id": agent_id,
            "device_id": device_id,
            "time": time,
            "value": value
        }
        collection.insert_one(point)

    def retrieve_last(self, measurement, agent_id, device_id):
        collection = self._client[measurement]
        q = {
            "agent_id": agent_id,
            "device_id": device_id
        }
        result = collection.find_one(q, sort=[('time', pymongo.DESCENDING)])
        if result is None:
            return {'value': None, 'time': None}
        else:
            return {'value': result['value'],
                    'time': result['time'].strftime('%Y-%m-%dT%H:%M:%SZ')}

    def retrieve_since(self, measurement, agent_id, device_id, since,
                       limit=10):
        pass

    def update(self, measurement, agent_id, device_id, time):
        pass
