# In The Name Of God
# ========================================
# [] File Name : thing.py
#
# [] Creation Date : 22-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================


class ThingNotFoundException(Exception):
    """
    Raised when a (rpi_id, device_id) requested that's not
    exists.
    """

    def __init__(self, rpi_id, device_id, type, error):
        super().__init__("(%s, %s) of type %s was Not Found." %
                         (rpi_id, device_id, type))
        self.rpi_id = rpi_id
        self.device_id = device_id
        self.type = type
        self.error = error