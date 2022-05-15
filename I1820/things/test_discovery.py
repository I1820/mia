from ..domain.agent import Agent, RawThing
from .discovery import DiscoveryService


def test_discovery():
    ds = DiscoveryService()

    things = {
        RawThing('fake_thing_1', 'lamp'),
        RawThing('fake_thing_2', 'lamp')
    }
    agent = Agent('fake_id', things=things, actions=[])

    ds.ping(agent)

    assert 'fake_id' in ds.agents
    assert ds.agents['fake_id']['things'] == [
        {'id': 'fake_thing_1', 'type': 'lamp'},
        {'id': 'fake_thing_2', 'type': 'lamp'},
    ]

    things = {
        RawThing('fake_thing_2', 'lamp')
    }
    agent = Agent('fake_id', things=things, actions=[])

    ds.ping(agent)

    assert 'fake_id' in ds.agents
    assert ds.agents['fake_id']['things'] == [
        {'id': 'fake_thing_2', 'type': 'lamp'},
    ]

    ds.pong('fake_id')

    assert 'fake_id' not in ds.agents
