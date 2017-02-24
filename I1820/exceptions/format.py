class InvalidLogFormatException(Exception):
    """
    Raised when a log with invalid format send to I1820.
    """

    def __init__(self, error):
        super().__init__("Invalid log format: %s" % str(error))
        self.error = error


class InvalidAgentFormatException(Exception):
    """
    Raised when a agent with invalid format send to I1820.
    """

    def __init__(self, error):
        super().__init__("Invalid agent format: %s" % str(error))
        self.error = error
