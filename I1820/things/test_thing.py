import typing

from ..controllers import NotificationController
from .base import Thing, Things
from .models.lamp import Lamp


class DummyMQTTService:
    def publish(self, body):
        pass

def test_get_thing():
    lamp = Things.get("lamp")

    assert lamp.name == 'lamp'
    assert isinstance(lamp, type)
    assert issubclass(lamp, Thing)
    assert issubclass(lamp, Lamp)
    assert isinstance(lamp('fake_agent', 'fake_device'), Lamp)
    assert isinstance(lamp('fake_agent', 'fake_device'), Thing)
    assert lamp.on.name == 'on'

    assert Things.things == {'lamp': lamp}

def test_trun_on_lamp():
    lamp = Things.get("lamp")

    NotificationController.mqtt_service = DummyMQTTService()

    assert issubclass(lamp, Lamp)
    l = lamp('fake_agent', 'fake_device')
    l.on = True
    assert l.on is True
