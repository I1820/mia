import dataclasses


@dataclasses.dataclass()
class MQTT:
    url: str


@dataclasses.dataclass()
class Appenders:
    name: str
    renew: bool


@dataclasses.dataclass()
class Config:
    mqtt: MQTT
    appenders: Appenders
