import pelix.framework
import logging


logger = logging.getLogger(__name__)

# Prepare the framework, with iPOPO
i1820_framework = pelix.framework.create_framework(
    ("pelix.ipopo.core",  "pelix.shell.core")
)

# Start the framework, and the pre-installed bundles
print(" * I1820 Framework is ready")
i1820_framework.start()
