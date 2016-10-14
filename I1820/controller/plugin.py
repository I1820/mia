# In The Name Of God
# ========================================
# [] File Name : plugin.py
#
# [] Creation Date : 29-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .base import I1820Controller
from ..plugins.base import Plugins

import threading


def plugin_runner(plugin, args: dict):
    plugin(**args)


class PluginController(I1820Controller):
    def __init__(self):
        self.plugins = []

    def new_plugin(self, name, args: dict):
        plugin = Plugins.get(name)
        p = threading.Thread(target=plugin_runner, args=(plugin, args),
                             name=name, deamon=True)
        p.start()
        self.plugins.append(p)

        return p.ident

    def list_plugin(self):
        results = {}

        for plugin in self.plugins:
            result = {}
            result['id'] = plugin.ident
            result['name'] = plugin.name
            result['is_alive'] = plugin.is_alive()

        return results
