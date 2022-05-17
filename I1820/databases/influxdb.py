from influxdb import InfluxDBClient

from .base import LogAppender


class InfluxdbLogAppender(LogAppender):
    def __init__(self, host, port, user, password, database):
        self._client = InfluxDBClient(host=host,
                                      port=port,
                                      username=user,
                                      password=password,
                                      database=database)

    def create(self, measurement, agent_id, device_id, time, value):
        points = [{
            "measurement": measurement,
            "tags": {
                "agent_id": agent_id,
                "device_id": device_id
            },
            "time": time.strftime('%Y-%m-%dT%H:%M:%SZ'),
            "fields": {
                "value": value
            }
        }]
        self._client.write_points(points, time_precision="s")

    def retrieve_last(self, measurement, agent_id, device_id):
        q = ('SELECT * FROM %s'
             ' WHERE "agent_id" = \'%s\' AND "device_id" = \'%s\''
             ' ORDER BY time DESC LIMIT 1;') % (measurement,
                                                agent_id, device_id)
        results = self._client.query(q)
        last = next(results.get_points(), None)
        if last is None:
            return {'value': None, 'time': None}
        else:
            return {'value': last['value'], 'time': last['time']}

    def retrieve_since(self, measurement, agent_id, device_id, since,
                       limit=10):
        q = ('SELECT * FROM %s'
             ' WHERE "agent_id" = \'%s\' AND "device_id" = \'%s\''
             ' AND time > \'%s\''
             ' ORDER BY time DESC LIMIT %d;') % (measurement, agent_id,
                                                 device_id, since, limit)
        results = self._client.query(q)
        next(results.get_points(), None)

    def update(self, measurement, agent_id, device_id, time):
        pass
