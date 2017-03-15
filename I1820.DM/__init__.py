import logging

i1820_log_format = (
    ('I1820.DM: [%(asctime)s] %(levelname)-8s %(name)-12s %(thread)-8s'
     ' %(message)s')
)

i1820_log_formatter = logging.Formatter(i1820_log_format)
i1820_log_handler = logging.StreamHandler()
i1820_log_handler.setLevel(logging.DEBUG)
i1820_log_handler.setFormatter(i1820_log_formatter)
logger = logging.getLogger('I1820')
logger.setLevel(logging.DEBUG)
logger.addHandler(i1820_log_handler)
