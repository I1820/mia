#!/usr/bin/env python3

from multiprocessing import Process

from I1820.http.main import main as http_main
from I1820.coap.main import main as coap_main


if __name__ == '__main__':
    p = Process(target=coap_main)
    p.start()
    http_main()
