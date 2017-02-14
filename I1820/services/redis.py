from ..conf.config import cfg

from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
     Validate, Invalidate, Instantiate


@ComponentFactory("redis_factory")
@Provides("redis_service")
@Property("default")
@Instantiate("default_redis_instance")
class RedisService:
    def __init__(self):
        self.rconn = None

    @Validate
    def validate(self, context):
        """
        The component is validated. This method is called right before the
        provided service is registered to the framework.
        """
        # All setup should be done here
        print(" * 18.20 Service: Redis Service")
        if cfg.redis_host == '-':
            print(" * Without Redis we are old but gold")
        else:
            import redis
            self.rconn = redis.StrictRedis(host=cfg.redis_host,
                                           port=int(cfg.redis_port))
            print(" * Redis at %s:%d" % (cfg.redis_host, int(cfg.redis_port)))

    @Invalidate
    def invalidate(self, context):
        """
        The component has been invalidated. This method is called right after
        the provided service has been removed from the framework.
        """
        pass
