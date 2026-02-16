import pytest
from src.notifications import send_notification

def test_invalid_email_format():
    '''Test that an invalid email format raises a ValueError'''
    invalid_emails = ["plainaddress", "missing@domain", "@missingusername.com", "username@.com"]
    for email in invalid_emails:
        with pytest.raises(ValueError):
            send_notification(email=email, order_id="123", total=10.0, tracking_number="ABC123")

def test_empty_order_id():
    '''Test that an empty order_id raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="valid@example.com", order_id="", total=10.0, tracking_number="ABC123")

def test_negative_total():
    '''Test that a negative total raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="valid@example.com", order_id="123", total=-10.0, tracking_number="ABC123")

def test_empty_tracking_number():
    '''Test that an empty tracking_number raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="valid@example.com", order_id="123", total=10.0, tracking_number="")

def test_zero_total():
    '''Test that a total of zero raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="valid@example.com", order_id="123", total=0.0, tracking_number="ABC123")

def test_null_email():
    '''Test that a null email raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email=None, order_id="123", total=10.0, tracking_number="ABC123")

def test_invalid_email_and_order_id():
    '''Test that invalid email and empty order_id prevents notification from being sent'''
    with pytest.raises(ValueError):
        send_notification(email="invalid_email", order_id="", total=10.0, tracking_number="ABC123")