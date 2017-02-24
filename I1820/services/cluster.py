# In The Name Of God
# ========================================
# [] File Name : cluster.py
#
# [] Creation Date : 24-02-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================

from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
     Validate, Invalidate, Instantiate, Requires


@ComponentFactory("cluster_factory")
@Provides("cluster_service")
@Property("default")
@Requires("_rs", "redis_service")
@Instantiate("default_cluster_instance")
class ClusterService:
    _code = {
        'el': 'core',
        'jj': 'scenario'
    }

    def __init__(self):
        self._rs = None
        self.name = None

    @Validate
    def validate(self, context):
        """
        The component is validated. This method is called right before the
        provided service is registered to the framework.
        """
        # All setup should be done here
        print(" * 18.20 Service: Cluster Service")

        # We are new to cluster
        n = self._rs.rconn.scard('i1820:')
        self._rs.rconn.client_setname('el-i1820-%d' % n)

        for client in self._rs.rconn.client_list():
            if client['name'] == self._rs.rconn.client_getname():
                name = 'el-i1820-%s' % client['addr'].split(':')[0]
                self._rs.rconn.sadd('i1820:', name)
                self._rs.rconn.client_setname(name)
                self.name = name
                break

    @Invalidate
    def invalidate(self, context):
        """
        The component has been invalidated. This method is called right after
        the provided service has been removed from the framework.
        """
        print(" > 18.20 Service: Cluster Service")
        self._rs.rconn.srem('i1820:', self._rs.rconn.client_getname())

    def neighbours(self):
        """
        Retrieves I1820 avaiable components
        """
        results = []

        for i1820 in self._rs.rconn.smembers('i1820:'):
            result = {}
            result['code'] = i1820
            result['type'], _, result['ip'] = i1820.split('-')
            result['type'] = ClusterService._code[result['type']]
            results.append(result)

        return results
