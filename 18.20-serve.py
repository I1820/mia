#!/usr/bin/env python3

from I1820.http.main import main as main_http
from I1820.mqtt.main import main as main_mqtt
from I1820.controllers.stat import StatController

if __name__ == '__main__':
    StatController()
    main_mqtt()
    main_http()
