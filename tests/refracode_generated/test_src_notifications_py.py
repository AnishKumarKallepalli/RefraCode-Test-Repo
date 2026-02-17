import pytest
from src.notifications import send_notification

def test_invalid_email_format():
    '''Test that an invalid email format raises a ValueError'''
    invalid_email = "invalid-email-format"
    order_id = "12345"
    total = 100.0
    tracking_number = "TRACK12345"
    with pytest.raises(ValueError):
        send_notification(email=invalid_email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_empty_order_id():
    '''Test that an empty order_id raises a ValueError'''
    email = "valid.email@example.com"
    order_id = ""
    total = 100.0
    tracking_number = "TRACK12345"
    with pytest.raises(ValueError):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_negative_total():
    '''Test that a negative total raises a ValueError'''
    email = "valid.email@example.com"
    order_id = "12345"
    total = -50.0
    tracking_number = "TRACK12345"
    with pytest.raises(ValueError):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_invalid_tracking_number_format():
    '''Test that an invalid tracking number format raises a ValueError'''
    email = "valid.email@example.com"
    order_id = "12345"
    total = 100.0
    tracking_number = "INVALID_TRACKING"
    with pytest.raises(ValueError):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_send_notification_with_invalid_email_and_order_id():
    '''Test that sending notification fails if email and order_id are invalid'''
    email = "invalid-email-format"
    order_id = ""
    total = 100.0
    tracking_number = "TRACK12345"
    with pytest.raises(ValueError):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_send_notification_with_none_email():
    '''Test that sending notification with None as email raises a ValueError'''
    email = None
    order_id = "12345"
    total = 100.0
    tracking_number = "TRACK12345"
    with pytest.raises(ValueError):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_send_notification_with_extreme_total():
    '''Test that an extremely large total raises a ValueError'''
    email = "valid.email@example.com"
    order_id = "12345"
    total = 1e+100  # Extremely large number
    tracking_number = "TRACK12345"
    with pytest.raises(ValueError):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)