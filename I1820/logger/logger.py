import logging

from rich.logging import RichHandler

logger = logging.getLogger("I1820")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "mia: [%(asctime)s] %(levelname)-8s %(name)-12s %(thread)-8s %(message)s"
)

handler = RichHandler(markup=True)
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

logger.addHandler(handler)
