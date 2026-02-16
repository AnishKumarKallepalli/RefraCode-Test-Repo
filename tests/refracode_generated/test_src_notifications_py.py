import pytest
from src.notifications import send_notification

def test_invalid_email_format():
    '''Test that an invalid email format raises an error'''
    invalid_email = "invalid-email-format"
    with pytest.raises(ValueError):
        send_notification(email=invalid_email, order_id="12345", total=10.0, tracking_number="TRACK123")

def test_empty_email():
    '''Test that an empty email raises an error'''
    empty_email = ""
    with pytest.raises(ValueError):
        send_notification(email=empty_email, order_id="12345", total=10.0, tracking_number="TRACK123")

def test_negative_total():
    '''Test that a negative total raises an error'''
    negative_total = -5.0
    with pytest.raises(ValueError):
        send_notification(email="test@example.com", order_id="12345", total=negative_total, tracking_number="TRACK123")

def test_zero_total():
    '''Test that a total of zero raises an error'''
    zero_total = 0.0
    with pytest.raises(ValueError):
        send_notification(email="test@example.com", order_id="12345", total=zero_total, tracking_number="TRACK123")

def test_invalid_order_id():
    '''Test that an invalid order_id format raises an error'''
    invalid_order_id = "!!!INVALID!!!"
    with pytest.raises(ValueError):
        send_notification(email="test@example.com", order_id=invalid_order_id, total=10.0, tracking_number="TRACK123")

def test_empty_order_id():
    '''Test that an empty order_id raises an error'''
    empty_order_id = ""
    with pytest.raises(ValueError):
        send_notification(email="test@example.com", order_id=empty_order_id, total=10.0, tracking_number="TRACK123")

def test_invalid_tracking_number_format():
    '''Test that an invalid tracking number format raises an error'''
    invalid_tracking_number = "12345-ABCDE"
    with pytest.raises(ValueError):
        send_notification(email="test@example.com", order_id="12345", total=10.0, tracking_number=invalid_tracking_number)

def test_send_notification_with_invalid_inputs():
    '''Test that no notification is sent when inputs are invalid'''
    invalid_email = "invalid-email-format"
    invalid_order_id = "!!!INVALID!!!"
    with pytest.raises(ValueError):
        send_notification(email=invalid_email, order_id=invalid_order_id, total=-10.0, tracking_number="TRACK123")