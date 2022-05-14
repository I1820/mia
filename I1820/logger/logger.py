import logging

from rich.logging import RichHandler

FORMAT = (
    'I1820: [%(asctime)s] %(levelname)-8s %(name)-12s %(thread)-8s %(message)s'
)


def setup():
    '''
    setup logging based on rich library and a custom format
    '''
    logging.basicConfig(
        level="NOTSET", format=FORMAT, datefmt="[%X]",
        handlers=[RichHandler(markup=True)]
    )
