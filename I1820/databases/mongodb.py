# In The Name Of God
# ========================================
# [] File Name : mongodb.py
#
# [] Creation Date : 21-03-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .base import I1820LogAppender
from ..conf.config import cfg

import pymongo


class MongodbLogAppender(I1820LogAppender):
    def __init__(self):
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
