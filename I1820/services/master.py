import pelix.framework
from pelix.utilities import use_service

class ServiceMaster:
    def __init__(self):
        self.i1820_framework = None
        self.i1820_framework_context = None

    def run(self):
        self.i1820_framework = pelix.framework.create_framework(
            ("pelix.ipopo.core",  "pelix.shell.core")
        )
        print(" * 18.20 Service Framework >>")
        self.i1820_framework.start()
        self.i1820_framework_context = self.i1820_framework.get_bundle_context()
        self.i1820_framework_context.install_bundle("I1820.services.stat").start()
        self.i1820_framework_context.install_bundle("I1820.services.model").start()
        print(" * 18.20 Service Framework <<")

    def service(self, service_name):
        service_ref = self.i1820_framework_context.get_service_reference(
            service_name)
        return use_service(self.i1820_framework_context, service_ref)
 

service_master = ServiceMaster()
