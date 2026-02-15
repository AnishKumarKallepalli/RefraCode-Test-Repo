import pytest
from src.notifications import send_notification

def test_invalid_email_format():
    '''Test that an invalid email format raises a ValueError'''
    invalid_emails = [
        "",  # empty string
        "plainaddress",  # missing '@' and domain
        "@missingusername.com",  # missing username
        "username@.com",  # missing domain name
        "username@domain..com",  # consecutive dots in domain
        "username@domain.com.",  # trailing dot
    ]
    for email in invalid_emails:
        with pytest.raises(ValueError):
            send_notification(email=email, order_id="12345", total=10.0, tracking_number="TRACK123")

def test_invalid_order_id():
    '''Test that an invalid order_id format raises a ValueError'''
    invalid_order_ids = [
        "",  # empty string
        "!!@#$$%",  # special characters
        "12345678901234567890123456789012345678901234567890",  # too long
        None,  # None value
    ]
    for order_id in invalid_order_ids:
        with pytest.raises(ValueError):
            send_notification(email="valid@example.com", order_id=order_id, total=10.0, tracking_number="TRACK123")

def test_negative_total_value():
    '''Test that a negative total raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="valid@example.com", order_id="12345", total=-10.0, tracking_number="TRACK123")

def test_zero_total_value():
    '''Test that a zero total raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="valid@example.com", order_id="12345", total=0.0, tracking_number="TRACK123")

def test_invalid_tracking_number_format():
    '''Test that an invalid tracking number format raises a ValueError'''
    invalid_tracking_numbers = [
        "",  # empty string
        "12345-67890-ABCDE",  # invalid format
        None,  # None value
    ]
    for tracking_number in invalid_tracking_numbers:
        with pytest.raises(ValueError):
            send_notification(email="valid@example.com", order_id="12345", total=10.0, tracking_number=tracking_number)

def test_notification_not_sent_on_invalid_email():
    '''Test that notification is not sent when email is invalid'''
    invalid_email = "invalid-email"
    result = send_notification(email=invalid_email, order_id="12345", total=10.0, tracking_number="TRACK123")
    assert result is None  # Assuming the function returns None when not sent

def test_notification_not_sent_on_invalid_order_id():
    '''Test that notification is not sent when order_id is invalid'''
    invalid_order_id = "!!@#$$%"
    result = send_notification(email="valid@example.com", order_id=invalid_order_id, total=10.0, tracking_number="TRACK123")
    assert result is None  # Assuming the function returns None when not sent

def test_notification_not_sent_on_negative_total():
    '''Test that notification is not sent when total is negative'''
    result = send_notification(email="valid@example.com", order_id="12345", total=-10.0, tracking_number="TRACK123")
    assert result is None  # Assuming the function returns None when not sent