import paho.mqtt.client as mqtt

from ..conf.config import Config
from ..things.discovery import DiscoveryService
from .route import Handler


class MQTTService():
    '''
    MQTTService handles the mqtt connection which is the way of communicating
    with agents and their things.
    '''

    def __init__(self, cfg: Config, discovery_service: DiscoveryService):
        self.client = mqtt.Client(client_id="i1820")
        self.hld = Handler(discovery_service, cfg)
        self.cfg = cfg

    def connect(self):
        '''
        connect into mqtt server
        '''
        try:
            self.client.connect(self.cfg.mqtt.host, self.cfg.mqtt.port, 60)
            print(f" * MQTT at {self.cfg.mqtt.host}:{self.cfg.mqtt.port}")
        except ConnectionError as exception:
            print(f" * MQTT at {self.cfg.mqtt.host}:{self.cfg.mqtt.port} had connection error.")
            raise exception

        # provides on connect handler
        self.client.on_connect = self.hld.on_connect

        self.client.loop_start()

    def die(self):
        '''
        disconnect from mqtt server
        '''
        print(" > MQTT Die")
        self.client.loop_stop()
