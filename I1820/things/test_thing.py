from .base import Thing, Things
from .models.lamp import Lamp


def test_get_thing():
    lamp = Things.get("lamp")

    assert lamp.name == 'lamp'
    assert isinstance(lamp, type)
    assert issubclass(lamp, Thing)
    assert issubclass(lamp, Lamp)
    assert isinstance(lamp('fake_agent', 'fake_device'), Lamp)
    assert isinstance(lamp('fake_agent', 'fake_device'), Thing)

    assert Things.things == {'lamp': lamp}

def test_trun_on_lamp():
    lamp = Things.get("lamp")

    assert issubclass(lamp, Lamp)
    l = lamp('fake_agent', 'fake_device')
    l.on = True
    assert l.on is True
