import os
import json

log_schema = json.load(open(os.path.join(os.path.dirname(__file__),
                                         "log.json")))
log_request_schema = json.load(open(os.path.join(os.path.dirname(__file__),
                                                 "log-request.json")))
