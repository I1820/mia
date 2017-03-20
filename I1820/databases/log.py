# In The Name Of God
# ========================================
# [] File Name : log.py
#
# [] Creation Date : 10-03-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import importlib

from ..conf.config import cfg
from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
     Validate, Invalidate, Instantiate


@ComponentFactory("log_factory")
@Provides("log_service")
@Property("default")
@Instantiate("default_log_instance")
class LogService:
    def __init__(self):
        self.appender = None

    @Validate
    def validate(self, context):
        """
        The component is validated. This method is called right before the
        provided service is registered to the framework.
        """
        # All setup should be done here
        print(" * 18.20 Service: Log Service")
        appender_name = cfg.appenders_appender
        appender_module = importlib.import_module(
            'I1820.appenders.%s' % appender_name)
        appender_cls = getattr(
            appender_module, "%sLogAppender" % appender_name.title())
        self.appender = appender_cls()

    @Invalidate
    def invalidate(self, context):
        """
        The component has been invalidated. This method is called right after
        the provided service has been removed from the framework.
        """
        pass

    def save(self, measurement, agent_id, device_id, time, value):
        last_value = None
        if cfg.appenders_renew == 'true':
            last_value = self.appender.last(measurement,
                                            agent_id, device_id)['value']

        if last_value is not None and value == last_value:
            return self.appender.renew(measurement, agent_id,
                                       device_id, time)
        else:
            return self.appender.save(measurement, agent_id,
                                      device_id, time, value)

    def last(self, measurement, agent_id, device_id):
        return self.appender.last(measurement, agent_id, device_id)
