import datetime

import pymongo
from pymongo.database import Database

from .base import LogAppender


class MongodbLogAppender(LogAppender):
    def __init__(self, host: str, port: int, database: str):
        self.client: pymongo.MongoClient = pymongo.MongoClient(host=host, port=port)
        self.database: Database = self.client[database]

    def create(
        self,
        measurement: str,
        agent_id: str,
        device_id: str,
        time: datetime.datetime,
        value,
    ):
        collection = self.database[measurement]
        point = {
            "agent_id": agent_id,
            "device_id": device_id,
            "time": time,
            "value": value,
        }
        collection.insert_one(point)

    def retrieve_last(self, measurement, agent_id, device_id):
        collection = self.database[measurement]
        q = {"agent_id": agent_id, "device_id": device_id}
        result = collection.find_one(q, sort=[("time", pymongo.DESCENDING)])
        if result is None:
            return {"value": None, "time": None}
        return {
            "value": result["value"],
            "time": result["time"].strftime("%Y-%m-%dT%H:%M:%SZ"),
        }

    def retrieve_since(self, measurement, agent_id, device_id, since, limit=10):
        pass
