from .discovery import DiscoveryController
from .stat import StatController


def main():
    print(" * I1820 controllers initiation")
    DiscoveryController()
    StatController()
