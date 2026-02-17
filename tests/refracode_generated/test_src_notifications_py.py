import pytest
from src.notifications import send_notification

def test_invalid_email_format():
    '''Test that an invalid email format raises a ValueError'''
    invalid_emails = ["plainaddress", "@missingusername.com", "username@.com", "username@domain..com"]
    for email in invalid_emails:
        with pytest.raises(ValueError):
            send_notification(email=email, order_id="12345", total=10.0, tracking_number="TRACK123")

def test_empty_order_id():
    '''Test that an empty order_id raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="test@example.com", order_id="", total=10.0, tracking_number="TRACK123")

def test_negative_total():
    '''Test that a negative total raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="test@example.com", order_id="12345", total=-5.0, tracking_number="TRACK123")

def test_zero_total():
    '''Test that a zero total raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="test@example.com", order_id="12345", total=0.0, tracking_number="TRACK123")

def test_invalid_tracking_number_format():
    '''Test that an invalid tracking number format raises a ValueError'''
    invalid_tracking_numbers = ["", "123", "TRACK-123-456-789", "TRACK@123"]
    for tracking_number in invalid_tracking_numbers:
        with pytest.raises(ValueError):
            send_notification(email="test@example.com", order_id="12345", total=10.0, tracking_number=tracking_number)

def test_notification_not_sent_on_invalid_input():
    '''Test that notification is not sent when inputs are invalid'''
    with pytest.raises(ValueError):
        send_notification(email="invalid_email", order_id="12345", total=10.0, tracking_number="TRACK123")

def test_exception_handling_during_email_sending():
    '''Test that exceptions during email sending are handled gracefully'''
    # Assuming send_email is a function that can raise an exception
    with pytest.raises(Exception):
        send_notification(email="test@example.com", order_id="12345", total=10.0, tracking_number="TRACK123", simulate_email_failure=True)