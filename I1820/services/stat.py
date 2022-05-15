import datetime
import resource


class StatService:
    def __init__(self):
        print(" * 18.20 Service: Stat Service")
        self.start_time = datetime.datetime.now()

    def uptime(self):
        return datetime.datetime.now() - self.start_time

    def resource(self):
        m = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        m = (m / 1000)
        return m
