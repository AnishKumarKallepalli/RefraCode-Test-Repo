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
    '''Test that a zero total raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="user@example.com", order_id="valid123", total=0.0, tracking_number="TRACK123")

def test_invalid_tracking_number_format():
    '''Test that an invalid tracking number format raises a ValueError'''
    invalid_tracking_numbers = ["", "12345", "TRACK-123-456-789-0-1-2"]
    for tracking_number in invalid_tracking_numbers:
        with pytest.raises(ValueError):
            send_notification(email="user@example.com", order_id="valid123", total=10.0, tracking_number=tracking_number)

def test_notification_not_sent_with_invalid_email():
    '''Test that notification is not sent if email is invalid'''
    invalid_email = "invalid_email_format"
    result = send_notification(email=invalid_email, order_id="valid123", total=10.0, tracking_number="TRACK123")
    assert result is None  # Assuming the function returns None when not sent

def test_notification_not_sent_with_invalid_order_id():
    '''Test that notification is not sent if order_id is invalid'''
    invalid_order_id = ""
    result = send_notification(email="user@example.com", order_id=invalid_order_id, total=10.0, tracking_number="TRACK123")
    assert result is None  # Assuming the function returns None when not sent

def test_notification_not_sent_with_negative_total():
    '''Test that notification is not sent if total is negative'''
    result = send_notification(email="user@example.com", order_id="valid123", total=-10.0, tracking_number="TRACK123")
    assert result is None  # Assuming the function returns None when not sent

def test_notification_not_sent_with_invalid_tracking_number():
    '''Test that notification is not sent if tracking number is invalid'''
    invalid_tracking_number = "INVALID_TRACKING"
    result = send_notification(email="user@example.com", order_id="valid123", total=10.0, tracking_number=invalid_tracking_number)
    assert result is None  # Assuming the function returns None when not sent