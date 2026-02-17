import pytest
from src.notifications import send_notification

def test_invalid_email_format():
    '''Test that an invalid email format raises a ValueError'''
    invalid_emails = ["plainaddress", "missing@domain", "@missingusername.com", "user@.com"]
    for email in invalid_emails:
        with pytest.raises(ValueError):
            send_notification(email=email, order_id="valid123", total=10.0, tracking_number="TRACK123")

def test_empty_order_id():
    '''Test that an empty order_id raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="user@example.com", order_id="", total=10.0, tracking_number="TRACK123")

def test_negative_total():
    '''Test that a negative total raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="user@example.com", order_id="valid123", total=-5.0, tracking_number="TRACK123")

def test_zero_total():
    '''Test that a total of zero raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="user@example.com", order_id="valid123", total=0.0, tracking_number="TRACK123")

def test_invalid_tracking_number_format():
    '''Test that an invalid tracking number format raises a ValueError'''
    invalid_tracking_numbers = ["", "12345", "TRACK-123-456-789", "TRACK@123"]
    for tracking_number in invalid_tracking_numbers:
        with pytest.raises(ValueError):
            send_notification(email="user@example.com", order_id="valid123", total=10.0, tracking_number=tracking_number)

def test_invalid_email_and_order_id_combination():
    '''Test that notifications are not sent if email and order_id are invalid'''
    with pytest.raises(ValueError):
        send_notification(email="invalid-email", order_id="!@#$%", total=10.0, tracking_number="TRACK123")