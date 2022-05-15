from ..domain.agent import Agent, RawThing
from .base import Things
from .discovery import DiscoveryService


def test_discovery():
    '''
    test discovery service which is responsible for register discovered things
    and then remove them when they are in-accessible for long period.
    '''
    ds = DiscoveryService()

    things = {
        RawThing('fake_thing_1', 'lamp'),
        RawThing('fake_thing_2', 'lamp')
    }
    agent = Agent('fake_id', things=things, actions=[])

    ds.ping(agent)

    assert 'fake_id' in ds.agents
    assert sorted([t['id'] for t in ds.agents['fake_id']['things']]) \
        == ['fake_thing_1', 'fake_thing_2']

    things = {
        RawThing('fake_thing_2', 'lamp')
    }
    agent = Agent('fake_id', things=things, actions=[])

    ds.ping(agent)

    assert 'fake_id' in ds.agents
    assert sorted([t['id'] for t in ds.agents['fake_id']['things']]) \
        == ['fake_thing_2']

    things = {
        RawThing('fake_thing_1', 'lamp'),
        RawThing('fake_thing_2', 'lamp'),
        RawThing('fake_thing_3', 'lamp')
    }
    agent = Agent('fake_id', things=things, actions=[])

    ds.ping(agent)

    assert 'fake_id' in ds.agents
    assert sorted([t['id'] for t in ds.agents['fake_id']['things']]) \
        == ['fake_thing_1', 'fake_thing_2', 'fake_thing_3']

    lamp = Things.get('lamp')
    assert 'lamp' in lamp.registered_things

    registered_lamps = lamp.registered_things['lamp']
    assert ('fake_id', 'fake_thing_1') in registered_lamps
    assert ('fake_id', 'fake_thing_2') in registered_lamps
    assert ('fake_id', 'fake_thing_3') in registered_lamps

    ds.pong('fake_id')

    assert 'fake_id' not in ds.agents

    lamp = Things.get('lamp')
    assert 'lamp' in lamp.registered_things

    registered_lamps = lamp.registered_things['lamp']
    assert len(registered_lamps) == 0
