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
    Raised when a (agent_id, device_id) is requested that is not
    exist.
    """

    def __init__(self, agent_id, device_id, type, error):
        super().__init__("(%s, %s) of type %s was Not Found." %
                         (agent_id, device_id, type))
        self.agent_id = agent_id
        self.device_id = device_id
        self.type = type
        self.error = error


class ThingTypeNotImplementedException(Exception):
    """
    Raised when a type of requested thing is not
    exist.
    """

    def __init__(self, type, error):
        super().__init__("type %s was Not Implemented." % type)
        self.type = type
        self.error = error


class ThingInvalidAccessException(Exception):
    """
    Raised when an invalid attribute is requested on thing.
    """

    def __init__(self, type, attribute):
        super().__init__("Invalid access on %s of type %s." %
                         (attribute, type))
        self.attribute = attribute
        self.type = type
