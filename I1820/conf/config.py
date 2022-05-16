'''
load configuration with validation.
'''

import dataclasses

from dynaconf import LazySettings, Validator


@dataclasses.dataclass()
class MQTT:
    host: str = '127.0.0.1'
    port: int = 1883


@dataclasses.dataclass()
class Config:
    tenant: str = 'main'
    mqtt: MQTT = MQTT()


def load() -> Config:
    '''
    loads configuration with validation into Config.
    each new configuration must be validated and then set into config.
    '''
    settings = LazySettings(
        settings_file=['config.toml'],
        envvar_prefix="MIA",
        nested_separator="__",
        validators=[
            Validator('mqtt.host', is_type_of=(str),
                      default='127.0.0.1'),
            Validator('mqtt.port', default=1883,
                      is_type_of=(int)),
            Validator('tenant', default="main",
                      is_type_of=(str))
        ]
    )

    cfg = Config()

    cfg.tenant = settings['tenant']
    cfg.mqtt.port = settings['mqtt.port']
    cfg.mqtt.host = settings['mqtt.host']

    return cfg
