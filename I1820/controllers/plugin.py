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

import uuid


class PluginController(I1820Controller):
    def __init__(self):
        self.chains = {}

    def on_log(self, log):
        for chain_id, chain in self.chains.items():
            for plugin in chain:
                if not plugin.on_log(log):
                    break

    def new_plugin(self, name: str, chain: int, args: dict):
        plugin = Plugins.get(name)
        ident = uuid.uuid4()
        p = plugin(ident, **args)
        if chain in self.chains:
            self.chains[chain].append(p)
        else:
            self.chains[chain] = [p]

        return p.ident

    def list_plugin(self):
        results = {}

        for chain_id, chain in self.chains.items():
            results[chain_id] = []
            for plugin in chain:
                result = {}
                result['id'] = str(plugin.ident)
                result['name'] = plugin.name
                results[chain_id].append(result)

        return results
