import pytest
from src.notifications import send_notification

def test_invalid_email_format():
    '''Test that an invalid email format raises a ValueError'''
    invalid_emails = ["plainaddress", "@missingusername.com", "username@.com"]
    for email in invalid_emails:
        with pytest.raises(ValueError):
            send_notification(email=email, order_id="12345", total=10.0, tracking_number="TRACK123")

def test_empty_order_id():
    '''Test that an empty order_id raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="user@example.com", order_id="", total=10.0, tracking_number="TRACK123")

def test_negative_total():
    '''Test that a negative total raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="user@example.com", order_id="12345", total=-10.0, tracking_number="TRACK123")

def test_zero_total():
    '''Test that a zero total raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="user@example.com", order_id="12345", total=0.0, tracking_number="TRACK123")

def test_invalid_tracking_number_format():
    '''Test that an invalid tracking number format raises a ValueError'''
    invalid_tracking_numbers = ["", "12345", "TRACK!@#"]
    for tracking_number in invalid_tracking_numbers:
        with pytest.raises(ValueError):
            send_notification(email="user@example.com", order_id="12345", total=10.0, tracking_number=tracking_number)

def test_notification_not_sent_with_invalid_email():
    '''Test that notifications are not sent if the email is invalid'''
    invalid_email = "invalid_email_format"
    result = send_notification(email=invalid_email, order_id="12345", total=10.0, tracking_number="TRACK123")
    assert result is False  # Assuming the function returns False when notification is not sent

def test_notification_not_sent_with_invalid_order_id():
    '''Test that notifications are not sent if the order_id is invalid'''
    invalid_order_id = ""
    result = send_notification(email="user@example.com", order_id=invalid_order_id, total=10.0, tracking_number="TRACK123")
    assert result is False  # Assuming the function returns False when notification is not sent

def test_notification_not_sent_with_negative_total():
    '''Test that notifications are not sent if the total is negative'''
    result = send_notification(email="user@example.com", order_id="12345", total=-5.0, tracking_number="TRACK123")
    assert result is False  # Assuming the function returns False when notification is not sent