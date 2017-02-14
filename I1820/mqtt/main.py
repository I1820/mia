# In The Name Of God
# ========================================
# [] File Name : main.py
#
# [] Creation Date : 12-10-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .route import client
from ..conf.config import cfg


def main():
    try:
        client.connect(cfg.mqtt_host, int(cfg.mqtt_port), 60)
        print(" * MQTT at %s:%d" % (cfg.mqtt_host, int(cfg.mqtt_port)))
    except ConnectionError as e:
        print(" * MQTT at %s:%d had connection error." % (cfg.mqtt_host,
                                                          int(cfg.mqtt_port)))
        raise e
    client.loop_start()
