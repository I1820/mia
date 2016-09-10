# In The Name Of God
# ========================================
# [] File Name : temperature.py
#
# [] Creation Date : 10-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .sensor import SensorThing


class Temprature(SensorThing):
    """
    This class represents Temperature sensor
    """
    name = "temperature"
    temperature = {}

    def __init__(self, rpi_id, device_id):
        self.rpi_id = rpi_id
        self.device_id = device_id

    @classmethod
    def new_thing(cls, rpi_id, device_id):
        cls.temperatures[(rpi_id, device_id)] = cls(rpi_id, device_id)
        print(cls)

    @classmethod
    def get_thing(cls, rpi_id, device_id):
        temperature = cls.temperatures[(rpi_id, device_id)]
        return temperature

    @property
    def temperature(self):
        """
        Temperature property is used for retrieve temperature data.
        """
        pass

    @temperature.setter
    def temperature(self, value):
        raise ValueError('Sensor states are not readable')
