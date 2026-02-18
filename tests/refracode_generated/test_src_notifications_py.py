from src.notifications import send_order_confirmation, send_shipping_notification
import pytest

def test_send_order_confirmation_invalid_email():
    # Validate that sending an order confirmation with an invalid email format raises an error
    with pytest.raises(ValueError):
        send_order_confirmation({'email': 'not-an-email', 'total': 10})

def test_send_order_confirmation_empty_email():
    # Validate that sending an order confirmation with an empty email raises an error
    with pytest.raises(ValueError):
        send_order_confirmation({'email': '', 'total': 10})

def test_send_order_confirmation_negative_total():
    # Validate that sending an order confirmation with a negative total raises an error
    with pytest.raises(ValueError):
        send_order_confirmation({'email': 'test@example.com', 'total': -10})

def test_send_order_confirmation_zero_total():
    # Validate that sending an order confirmation with a total of zero raises an error
    with pytest.raises(ValueError):
        send_order_confirmation({'email': 'test@example.com', 'total': 0})

def test_send_shipping_notification_empty_tracking_number():
    # Validate that sending a shipping notification with an empty tracking number raises an error
    with pytest.raises(ValueError):
        send_shipping_notification({'tracking_number': ''})

def test_send_shipping_notification_invalid_tracking_number():
    # Validate that sending a shipping notification with an invalid tracking number raises an error
    with pytest.raises(ValueError):
        send_shipping_notification({'tracking_number': 'invalid-tracking'})