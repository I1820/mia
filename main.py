'''
runs mia server
'''

from rich import pretty
from rich.console import Console

import I1820.conf

if __name__ == '__main__':
    console = Console()
    pretty.install()

    cfg = I1820.conf.load()
    pretty.pprint(cfg)

    console.print("Mia is up and running", style="bold red")
