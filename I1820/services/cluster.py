# In The Name Of God
# ========================================
# [] File Name : cluster.py
#
# [] Creation Date : 24-02-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from ..conf.config import cfg

from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
     Validate, Invalidate, Instantiate
import consul


@ComponentFactory("cluster_factory")
@Provides("cluster_service")
@Property("default")
@Instantiate("default_cluster_instance")
class ClusterService:
    def __init__(self):
        self.name = None
        self.consulc = None

    @Validate
    def validate(self, context):
        """
        The component is validated. This method is called right before the
        provided service is registered to the framework.
        """
        # All setup should be done here
        self.consulc = consul.Client(endpoint="http://192.168.73.8:8500")
        self.consulc.register(id='el1', name='I1820.core',
                              address='192.168.73.5', port=8080,
                              tags=('el1', 'core', 'v3'),
                              check={'id': 'core', 'name': 'core on port 8080',
                                     'tcp': '192.168.73.5:8080',
                                     'Interval': '30s', 'timeout': '2s'})
        print(" * 18.20 Service: Cluster Service")

    @Invalidate
    def invalidate(self, context):
        """
        The component has been invalidated. This method is called right after
        the provided service has been removed from the framework.
        """
        self.consulc.deregister(id='el1')
        print(" > 18.20 Service: Cluster Service")

    @property
    def tenant(self):
        result = {
            'id': cfg.tenant_id,
            'owner': cfg.tenant_owner
        }
        return result
