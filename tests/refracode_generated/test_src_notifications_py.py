import pytest
from src.notifications import send_notification

def test_invalid_email_format():
    '''Test that an invalid email format raises a ValueError'''
    invalid_email = "invalid_email_format"
    with pytest.raises(ValueError):
        send_notification(email=invalid_email, order_id="12345", total=10.0, tracking_number="TRACK123")

def test_empty_email():
    '''Test that an empty email raises a ValueError'''
    empty_email = ""
    with pytest.raises(ValueError):
        send_notification(email=empty_email, order_id="12345", total=10.0, tracking_number="TRACK123")

def test_negative_total():
    '''Test that a negative total raises a ValueError'''
    negative_total = -5.0
    with pytest.raises(ValueError):
        send_notification(email="test@example.com", order_id="12345", total=negative_total, tracking_number="TRACK123")

def test_zero_total_for_order_confirmation():
    '''Test that a zero total raises a ValueError for order confirmation'''
    zero_total = 0.0
    with pytest.raises(ValueError):
        send_notification(email="test@example.com", order_id="12345", total=zero_total, tracking_number="TRACK123", order_confirmation=True)

def test_invalid_order_id_format():
    '''Test that an invalid order_id format raises a ValueError'''
    invalid_order_id = "!!@#$$%"
    with pytest.raises(ValueError):
        send_notification(email="test@example.com", order_id=invalid_order_id, total=10.0, tracking_number="TRACK123")

def test_invalid_tracking_number_format():
    '''Test that an invalid tracking_number format raises a ValueError'''
    invalid_tracking_number = "123-XYZ"
    with pytest.raises(ValueError):
        send_notification(email="test@example.com", order_id="12345", total=10.0, tracking_number=invalid_tracking_number)

def test_large_negative_total():
    '''Test that a very large negative total raises a ValueError'''
    large_negative_total = -1e10
    with pytest.raises(ValueError):
        send_notification(email="test@example.com", order_id="12345", total=large_negative_total, tracking_number="TRACK123")

def test_null_email():
    '''Test that a null email raises a ValueError'''
    null_email = None
    with pytest.raises(ValueError):
        send_notification(email=null_email, order_id="12345", total=10.0, tracking_number="TRACK123")