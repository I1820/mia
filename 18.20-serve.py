#!/usr/bin/env python3

from I1820.http.main import main as main_http
from I1820.mqtt.main import main as main_mqtt
from I1820.mqtt.main import die as die_mqtt
from I1820.services.main import main as main_srv
from I1820.services.main import die as die_srv

if __name__ == '__main__':
    print(' * 18.20 at Sep 07 2016 7:20 IR721')
    main_srv()
    main_mqtt()
    try:
        main_http()
    except KeyboardInterrupt:
        print(" > 18.20 As always ... left me alone")
        die_mqtt()
        die_srv()
