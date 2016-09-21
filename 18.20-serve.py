#!/usr/bin/env python3

import threading

from I1820.http.main import main as http_main
from I1820.coap.main import main as coap_main


if __name__ == '__main__':
    http_thread = threading.Thread(target=http_main)
    coap_thread = threading.Thread(target=coap_main)
    http_thread.start()
    coap_thread.start()
