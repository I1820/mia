'''
this module loads json schemas from the files and used
for validating incoming mqtt requests.
'''

import json
import os

log_schema = json.load(
    open(
        os.path.join(os.path.dirname(__file__), "log.json"),
        encoding="UTF-8"
    ))

agent_schema = json.load(
    open(
        os.path.join(os.path.dirname(__file__), "agent.json"),
        encoding="UTF-8"
    ))
