import pytest
from src.notifications import send_notification

def test_invalid_email_format():
    '''Test that an invalid email format raises a ValueError'''
    invalid_email = "invalid_email_format"
    order_id = "12345"
    total = 10.0
    tracking_number = "TRACK123"
    with pytest.raises(ValueError):
        send_notification(email=invalid_email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_empty_order_id():
    '''Test that an empty order_id raises a ValueError'''
    email = "test@example.com"
    order_id = ""
    total = 10.0
    tracking_number = "TRACK123"
    with pytest.raises(ValueError):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_negative_total_value():
    '''Test that a negative total raises a ValueError'''
    email = "test@example.com"
    order_id = "12345"
    total = -5.0
    tracking_number = "TRACK123"
    with pytest.raises(ValueError):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_invalid_tracking_number_format():
    '''Test that an invalid tracking number format raises a ValueError'''
    email = "test@example.com"
    order_id = "12345"
    total = 10.0
    tracking_number = "INVALID_TRACKING"
    with pytest.raises(ValueError):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_send_notification_with_invalid_inputs():
    '''Test that notification is not sent when inputs are invalid'''
    email = "invalid_email"
    order_id = "12345"
    total = 10.0
    tracking_number = "TRACK123"
    # Assuming send_notification has a return value indicating success
    result = send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)
    assert result is False  # Expecting notification not to be sent

def test_zero_total_value():
    '''Test that a zero total raises a ValueError'''
    email = "test@example.com"
    order_id = "12345"
    total = 0.0
    tracking_number = "TRACK123"
    with pytest.raises(ValueError):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)