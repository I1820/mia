# In The Name Of God
# ========================================
# [] File Name : kafka.py
#
# [] Creation Date : 03-12-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .base import I1820LogAppender
from ..conf.config import cfg

from kafka import KafkaProducer
import json


class KafkaLogAppender(I1820LogAppender):
    def __init__(self):
        bootstrap_servers = "%s:%s" % (cfg.appenders_kafka_host,
                                       cfg.appenders_kafka_port)
        self.producer = KafkaProducer(value_serializer=self.json_serializer,
                                      bootstrap_servers=bootstrap_servers)

    def save(self, measurement, agent_id, device_id, time, value):
        data = {
            "tags": {
                "agent_id": agent_id,
                "device_id": device_id
            },
            "time": time.strftime('%Y-%m-%dT%H:%M:%SZ'),
            "fields": {
                "value": value
            }
        }
        self.producer.send(measurement, data).get(timeout=60)

    def last(self, measurement, agent_id, device_id):
        return {'value': None, 'time': None}

    def since(self, measurement, agent_id, device_id, since, limit=10):
        return None

    @staticmethod
    def json_serializer(v):
        return json.dumps(v).encode('utf-8')
