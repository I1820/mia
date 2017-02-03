# In The Name Of God
# ========================================
# [] File Name : stat.py
#
# [] Creation Date : 22-11-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import datetime

from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
         Validate, Invalidate, Instantiate


@ComponentFactory("stat_factory")
@Provides("stat_service")
@Property("default")
@Instantiate("stat_instance")
class StatService:
    def __init__(self):
        self.start_time = None

    @Validate
    def validate(self, context):
        """
        The component is validated. This method is called right before the
        provided service is registered to the framework.
        """
        # All setup should be done here
        print(" * 18.20 Service: Stat Service")
        self.start_time = datetime.datetime.now()

    @Invalidate
    def invalidate(self, context):
        """
        The component has been invalidated. This method is called right after
        the provided service has been removed from the framework.
        """
        self.start_time = None

    def uptime(self):
        return datetime.datetime.now() - self.start_time
