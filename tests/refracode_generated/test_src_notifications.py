import pytest
from src.notifications import send_order_confirmation, send_shipping_notification

def test_send_order_confirmation_happy_path():
    # Valid inputs return True
    assert send_order_confirmation(order_id="123", email="test@example.com", total=10.0) is True

def test_send_order_confirmation_none_email_raises():
    # None email raises ValueError
    with pytest.raises(ValueError):
        send_order_confirmation(order_id="123", email=None, total=10.0)

def test_send_order_confirmation_empty_email_raises():
    # Empty email raises ValueError
    with pytest.raises(ValueError):
        send_order_confirmation(order_id="123", email="", total=10.0)

def test_send_order_confirmation_invalid_email_raises():
    # Invalid email raises ValueError
    with pytest.raises(ValueError):
        send_order_confirmation(order_id="123", email="invalidemail", total=10.0)

def test_send_order_confirmation_zero_total_raises():
    # Zero total raises ValueError
    with pytest.raises(ValueError):
        send_order_confirmation(order_id="123", email="test@example.com", total=0.0)

def test_send_order_confirmation_negative_total_raises():
    # Negative total raises ValueError
    with pytest.raises(ValueError):
        send_order_confirmation(order_id="123", email="test@example.com", total=-1)

def test_send_shipping_notification_happy_path():
    # Valid inputs return True
    assert send_shipping_notification(tracking_number="ABCD1234", email="test@example.com") is True

def test_send_shipping_notification_none_tracking_number_raises():
    # None tracking number raises ValueError
    with pytest.raises(ValueError):
        send_shipping_notification(tracking_number=None, email="test@example.com")

def test_send_shipping_notification_empty_tracking_number_raises():
    # Empty tracking number raises ValueError
    with pytest.raises(ValueError):
        send_shipping_notification(tracking_number="", email="test@example.com")

def test_send_shipping_notification_invalid_tracking_number_raises():
    # Invalid tracking number raises ValueError
    with pytest.raises(ValueError):
        send_shipping_notification(tracking_number="123", email="test@example.com")

def test_send_shipping_notification_none_email_raises():
    # None email raises ValueError
    with pytest.raises(ValueError):
        send_shipping_notification(tracking_number="ABCD1234", email=None)

def test_send_shipping_notification_empty_email_raises():
    # Empty email raises ValueError
    with pytest.raises(ValueError):
        send_shipping_notification(tracking_number="ABCD1234", email="")

def test_send_shipping_notification_invalid_email_raises():
    # Invalid email raises ValueError
    with pytest.raises(ValueError):
        send_shipping_notification(tracking_number="ABCD1234", email="invalidemail")