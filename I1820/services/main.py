from .master import service_master


def main():
    service_master.run()


def die():
    service_master.stop()
