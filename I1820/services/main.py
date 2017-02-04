import pelix.framework


def main():
    i1820_framework = pelix.framework.create_framework(
        ("pelix.ipopo.core",  "pelix.shell.core")
    )
    print(" * 18.20 Service Framework >>")
    i1820_framework.start()
    i1820_framework_context = i1820_framework.get_bundle_context()
    i1820_framework_context.install_bundle("I1820.controllers.stat").start()
    i1820_framework_context.install_bundle("I1820.controllers.model").start()
    print(" * 18.20 Service Framework <<")
