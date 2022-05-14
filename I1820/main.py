from I1820.http.main import die as die_http
from I1820.http.main import main as main_http
from I1820.mqtt.main import die as die_mqtt
from I1820.mqtt.main import main as main_mqtt
from I1820.services.main import die as die_srv
from I1820.services.main import main as main_srv

if __name__ == '__main__':
    main_srv()
    main_mqtt()
    try:
        main_http()
    except KeyboardInterrupt:
        die_http()
        die_mqtt()
        die_srv()
