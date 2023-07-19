"""
load configuration with validation.
"""

import dataclasses

from dynaconf import LazySettings, Validator


@dataclasses.dataclass()
class MQTT:
    host: str = "127.0.0.1"
    port: int = 1883


@dataclasses.dataclass()
class MongoDBDatabase:
    host: str = "mongodb://127.0.0.1"
    port: int = 23017
    database: str = "mia"


@dataclasses.dataclass()
class InfluxDBDatabase:
    host: str = "127.0.0.1"
    port: int = 8080
    database: str = "mia"
    username: str = "admin"
    password: str = "admin"


@dataclasses.dataclass()
class Database:
    name: str = "mongodb"
    config: MongoDBDatabase | InfluxDBDatabase = dataclasses.field(
        default_factory=MongoDBDatabase
    )


@dataclasses.dataclass()
class Config:
    tenant: str = "main"
    mqtt: MQTT = dataclasses.field(default_factory=MQTT)
    database: Database = dataclasses.field(default_factory=Database)


def load() -> Config:
    """
    loads configuration with validation into Config.
    each new configuration must be validated and then set into config.
    """
    settings = LazySettings(
        settings_file=["config.toml"],
        envvar_prefix="MIA",
        nested_separator="__",
        validators=[
            Validator(
                "database.name",
                is_type_of=(str),
                is_in=("mongodb", "influxdb"),
                default="mongodb",
            ),
            Validator(
                "database.config.host",
                is_type_of=(str),
                default="mongodb://127.0.0.1",
            ),
            Validator("database.config.port", is_type_of=(int), default=27017),
            Validator(
                "database.config.database", is_type_of=(str), default="mia"
            ),
            Validator("mqtt.host", is_type_of=(str), default="127.0.0.1"),
            Validator("mqtt.port", default=1883, is_type_of=(int)),
            Validator("tenant", default="main", is_type_of=(str)),
        ],
    )

    cfg = Config()

    cfg.tenant = settings["tenant"]
    cfg.mqtt.port = settings["mqtt.port"]
    cfg.mqtt.host = settings["mqtt.host"]
    cfg.database.name = settings["database.name"]

    match cfg.database.name:
        case "mongodb":
            cfg.database.config = MongoDBDatabase()
            cfg.database.config.host = settings["database.config.host"]
            cfg.database.config.port = settings["database.config.port"]
            cfg.database.config.database = settings["database.config.database"]
        case "influxdb":
            cfg.database.config = InfluxDBDatabase()
            cfg.database.config.host = settings["database.config.host"]
            cfg.database.config.port = settings["database.config.port"]
            cfg.database.config.database = settings["database.config.database"]
            cfg.database.config.username = settings["database.config.username"]
            cfg.database.config.password = settings["database.config.password"]

    return cfg
