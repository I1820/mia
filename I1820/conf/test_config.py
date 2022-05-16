import os

from .config import load


def test_loading():
    cfg = load()

    assert cfg.tenant == 'main'
    assert cfg.mqtt.host == '127.0.0.1'
    assert cfg.mqtt.port == 1883

def test_loading_with_env():
    os.environ['MIA_TENANT'] = 'mia'
    os.environ['MIA_MQTT__HOST'] = 'localhost'

    cfg = load()

    assert cfg.tenant == 'mia'
    assert cfg.mqtt.host == 'localhost'
    assert cfg.mqtt.port == 1883
