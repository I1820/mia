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
import uuid


class PluginController(I1820Controller):
    def __init__(self):
        self.plugins = []

    def on_log(self, log):
        for plugin in self.plugins:
            threading.Thread(target=plugin.on_log, args=(log,),
                             daemon=True).start()

    def new_plugin(self, name, args: dict):
        plugin = Plugins.get(name)
        ident = uuid.uuid4()
        p = plugin(ident, **args)
        self.plugins.append(p)

        return p.ident

    def list_plugin(self):
        results = []

        for plugin in self.plugins:
            result = {}
            result['id'] = str(plugin.ident)
            result['name'] = plugin.name
            results.append(result)

        return results
