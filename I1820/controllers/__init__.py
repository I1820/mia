import pelix.framework
import logging


logger = logging.getLogger(__name__)

# Prepare the framework, with iPOPO
i1820_framework = pelix.framework.create_framework((
    # iPOPO
    "pelix.ipopo.core")
)

# Start the framework, and the pre-installed bundles
logger.info('I1820 Framework was started :P')
i1820_framework.start()
