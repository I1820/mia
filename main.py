"""
runs mia server
"""

import typing

from rich import pretty
from rich.console import Console

import I1820.conf
import I1820.controllers
import I1820.databases
import I1820.discovery
import I1820.http.main
import I1820.logger
import I1820.mqtt

# just for type hinting
from I1820.conf.config import InfluxDBDatabase, MongoDBDatabase

if __name__ == "__main__":
    console = Console()
    pretty.install()

    cfg = I1820.conf.load()
    pretty.pprint(cfg)

    database: I1820.databases.LogAppender

    match cfg.database.name:
        case "mongodb":
            cfg.database.config = typing.cast(
                MongoDBDatabase, cfg.database.config
            )
            database = I1820.databases.MongodbLogAppender(
                host=cfg.database.config.host,
                port=cfg.database.config.port,
                database=cfg.database.config.database,
            )
        case "influxdb":
            cfg.database.config = typing.cast(
                InfluxDBDatabase, cfg.database.config
            )
            database = I1820.databases.InfluxdbLogAppender(
                host=cfg.database.config.host,
                port=cfg.database.config.port,
                database=cfg.database.config.database,
                user=cfg.database.config.username,
                password=cfg.database.config.password,
            )
        case _:
            raise ValueError("invalid database type")

    log_service = I1820.databases.LogService(database)

    discovery_service = I1820.discovery.DiscoveryService()
    mqtt_service = I1820.mqtt.MQTTService(
        cfg.mqtt.host, cfg.mqtt.port, cfg.tenant, discovery_service
    )
    mqtt_service.connect()

    # i don't know is there any a better way or not
    I1820.controllers.NotificationController.mqtt_service = mqtt_service
    I1820.controllers.LogController.log_service = log_service

    console.print("Mia is up and running", style="bold red")

    app = I1820.http.main.app(discovery_service)
    app.run(host="0.0.0.0", port=8080, fast=True)
