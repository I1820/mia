#!/usr/bin/env python3

from I1820.http.main import main as main_http
from I1820.mqtt.main import main as main_mqtt

if __name__ == '__main__':
    main_mqtt()
    main_http()
