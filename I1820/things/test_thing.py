from ..controllers import NotificationController
from .base import Thing, Things
from .fields.base import Field
from .models.lamp import Lamp


class DummyMQTTService:
    def publish(self, body):
        pass

def test_get_thing():
    lamp = Things.get("lamp")
    light = Things.get("light")

    assert lamp.name == 'lamp'
    assert isinstance(lamp, type)
    assert issubclass(lamp, Thing)
    assert issubclass(lamp, Lamp)
    assert isinstance(lamp('fake_agent', 'fake_device'), Lamp)
    assert isinstance(lamp('fake_agent', 'fake_device'), Thing)
    assert lamp.__dict__['on'].name == 'on'
    assert isinstance(lamp.__dict__['on'], Field)

    assert len(Things.things)
    assert Things.things['lamp'] == lamp
    assert Things.things['light'] == light

    assert len(lamp.registered_things) == 2
    assert "lamp" in lamp.registered_things

def test_trun_on_lamp():
    lamp = Things.get("lamp")

    NotificationController.mqtt_service = DummyMQTTService()

    assert issubclass(lamp, Lamp)
    l = lamp('fake_agent', 'fake_device')
    l.on = True
    assert l.on is True
