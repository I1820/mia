import dataclasses


@dataclasses.dataclass()
class MQTT:
    host: str
    port: int


@dataclasses.dataclass()
class Appenders:
    name: str
    renew: bool


@dataclasses.dataclass()
class Config:
    tenant: str
    mqtt: MQTT
    appenders: Appenders
