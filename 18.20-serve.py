#!/usr/bin/env python3

from multiprocessing import Process

from I1820.http.main import main as http_main
from I1820.ws.main import main as ws_main


if __name__ == '__main__':
    Process(target=ws_main).start()
    http_main()
