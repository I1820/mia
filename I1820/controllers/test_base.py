from .notif import NotificationController


def test_controller():
    ntc1 = NotificationController()
    ntc2 = NotificationController()

    assert ntc1 == ntc2
