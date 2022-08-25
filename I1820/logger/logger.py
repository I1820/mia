import logging

from rich.logging import RichHandler

logger = logging.getLogger(__name__)

formatter = logging.Formatter(
    "mia: [%(asctime)s] %(levelname)-8s %(name)-12s %(thread)-8s %(message)s"
)

handler = RichHandler(markup=True)
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)

logger.addHandler(handler)
