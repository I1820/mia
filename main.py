'''
runs mia server
'''

from rich import pretty
from rich.console import Console

import I1820.conf
import I1820.discovery
import I1820.http.main
import I1820.logger
import I1820.mqtt

if __name__ == '__main__':
    I1820.logger.setup()

    console = Console()
    pretty.install()

    cfg = I1820.conf.load()
    pretty.pprint(cfg)

    discovery_service = I1820.discovery.DiscoveryService()
    mqtt_service = I1820.mqtt.MQTTService(cfg.mqtt.host, cfg.mqtt.port,
                                          cfg.tenant, discovery_service)
    mqtt_service.connect()

    console.print("Mia is up and running", style="bold red")

    app = I1820.http.main.app()
    app.run(host="0.0.0.0", port=8080)
