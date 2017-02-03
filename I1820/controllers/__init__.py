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

# Get the bundle context of the framework, i.e. the link between the
# framework starter and its content.
i1820_framework_context = i1820_framework.get_bundle_context()


# Service Initiation
# Stat service
i1820_framework_context.install_bundle("I1820.controllers.stat").start()
