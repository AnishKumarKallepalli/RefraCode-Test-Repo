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
    email = "valid.email@example.com"
    order_id = ""
    total = 10.0
    tracking_number = "TRACK123"
    with pytest.raises(ValueError):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_negative_total_value():
    '''Test that a negative total raises a ValueError'''
    email = "valid.email@example.com"
    order_id = "12345"
    total = -5.0
    tracking_number = "TRACK123"
    with pytest.raises(ValueError):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_invalid_tracking_number_format():
    '''Test that an invalid tracking number format raises a ValueError'''
    email = "valid.email@example.com"
    order_id = "12345"
    total = 10.0
    tracking_number = "INVALID_TRACKING"
    with pytest.raises(ValueError):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_null_email():
    '''Test that a null email raises a ValueError'''
    email = None
    order_id = "12345"
    total = 10.0
    tracking_number = "TRACK123"
    with pytest.raises(ValueError):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_zero_total_value():
    '''Test that a zero total raises a ValueError'''
    email = "valid.email@example.com"
    order_id = "12345"
    total = 0.0
    tracking_number = "TRACK123"
    with pytest.raises(ValueError):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_order_id_with_special_characters():
    '''Test that an order_id with special characters raises a ValueError'''
    email = "valid.email@example.com"
    order_id = "ORDER@ID!"
    total = 10.0
    tracking_number = "TRACK123"
    with pytest.raises(ValueError):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_notifications_not_sent_with_invalid_email():
    '''Test that notifications are not sent if email is invalid'''
    email = "invalid_email_format"
    order_id = "12345"
    total = 10.0
    tracking_number = "TRACK123"
    # Assuming send_notification returns False if notification is not sent
    result = send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)
    assert result is False

def test_notifications_not_sent_with_invalid_order_id():
    '''Test that notifications are not sent if order_id is invalid'''
    email = "valid.email@example.com"
    order_id = ""
    total = 10.0
    tracking_number = "TRACK123"
    result = send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)
    assert result is False

def test_notifications_not_sent_with_negative_total():
    '''Test that notifications are not sent if total is negative'''
    email = "valid.email@example.com"
    order_id = "12345"
    total = -10.0
    tracking_number = "TRACK123"
    result = send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)
    assert result is False