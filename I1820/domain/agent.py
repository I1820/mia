import dataclasses
import datetime
import json

import jsonschema

from ..exceptions.format import InvalidAgentFormatException
from .schemas.schema import agent_schema


@dataclasses.dataclass(frozen=True)
class RawThing:
    '''
    RawThing represents a thing that is attached into an agent.
    This is a very low level interface and we will convert 
    it into our models later.
    '''
    id: str
    type: str


class Agent:
    '''
    The Agent object contains information that is used to
    represents agent to our platform.
    '''
    def __init__(self, ident: str, things: set[RawThing], actions: list[str]):
        self.ident = ident
        self.things = things
        self.actions = actions
        self.last_seen: datetime.datetime

    def to_json(self):
        '''
        convert an agent into json representation
        '''
        result = {
            'id': self.ident,
            'things': [dataclasses.asdict(t) for t in self.things],
            'actions': self.actions
        }
        return json.dumps(result)

    @classmethod
    def from_json(cls, raw):
        raw_values = json.loads(raw)

        # validate input json
        try:
            jsonschema.validate(raw_values, agent_schema)
        except jsonschema.ValidationError as e:
            raise InvalidAgentFormatException(e)

        ident = raw_values['id']
        things: set[RawThing] = set()
        for raw_thing in raw_values['things']:
            things.add(
                RawThing(id=raw_thing['id'], type=raw_thing['type'])
            )
        actions = []
        if 'actions' in raw_values:
            actions = raw_values['actions']
        return cls(ident, things, actions)
