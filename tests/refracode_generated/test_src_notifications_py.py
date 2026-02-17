import pytest
from src.notifications import send_notification

def test_invalid_email_format():
    '''Test that an invalid email format raises a ValueError'''
    invalid_emails = ["plainaddress", "missing@domain", "@missingusername.com", "username@.com"]
    for email in invalid_emails:
        with pytest.raises(ValueError):
            send_notification(email=email, order_id="valid_order", total=10.0, tracking_number="valid_tracking")

def test_empty_order_id():
    '''Test that an empty order_id raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="valid@example.com", order_id="", total=10.0, tracking_number="valid_tracking")

def test_negative_total():
    '''Test that a negative total raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="valid@example.com", order_id="valid_order", total=-10.0, tracking_number="valid_tracking")

def test_empty_tracking_number():
    '''Test that an empty tracking_number raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="valid@example.com", order_id="valid_order", total=10.0, tracking_number="")

def test_zero_total():
    '''Test that a zero total raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="valid@example.com", order_id="valid_order", total=0.0, tracking_number="valid_tracking")

def test_invalid_email_and_order_id():
    '''Test that notifications are not sent if email and order_id are invalid'''
    with pytest.raises(ValueError):
        send_notification(email="invalid_email", order_id="", total=10.0, tracking_number="valid_tracking")

def test_exception_handling_during_email_sending():
    '''Test that exceptions during email sending are handled gracefully'''
    # Assuming send_email raises an exception for certain email formats
    with pytest.raises(Exception):
        send_notification(email="valid@example.com", order_id="valid_order", total=10.0, tracking_number="valid_tracking", simulate_failure=True)