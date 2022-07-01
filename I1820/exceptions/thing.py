from sanic.exceptions import SanicException


class ThingNotFoundException(SanicException):
    """
    raised when a (agent_id, device_id) is requested that is not
    exist.
    """
    status_code = 404

    def __init__(self, agent_id, device_id, device_type, error):

        super().__init__(
            message=f"({agent_id}, {device_id}) of type {device_type} "
            "was Not Found."
        )
        self.agent_id = agent_id
        self.device_id = device_id
        self.device_type = device_type
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
