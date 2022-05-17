import paho.mqtt.client as mqtt

from ..discovery import DiscoveryService
from .route import Handler


class MQTTService():
    '''
    MQTTService handles the mqtt connection which is the way of communicating
    with agents and their things.
    '''

    def __init__(self, host: str, port: int, tenant: str,
                 discovery_service: DiscoveryService):
        self.client = mqtt.Client(client_id="i1820")
        self.hld = Handler(discovery_service, tenant)
        self.host = host
        self.port = port

    def connect(self):
        '''
        connect into mqtt server
        '''
        try:
            self.client.connect(self.host, self.port, 60)
            print(f" * MQTT at {self.host}:{self.port}")
        except Exception as exception:
            print(f" * MQTT at {self.host}:{self.port} had connection error.")
            raise exception

        # provides on connect handler
        self.client.on_connect = self.hld.on_connect

        self.client.loop_start()


    def publish(self, body: str):
        self.hld.publish(self.client, body)

    def die(self):
        '''
        disconnect from mqtt server
        '''
        print(" > MQTT Die")
        self.client.loop_stop()
