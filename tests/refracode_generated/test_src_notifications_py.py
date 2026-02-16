import pytest
from src.notifications import send_notification

def test_invalid_email_format():
    '''Test that an invalid email format raises a ValueError'''
    invalid_emails = [
        "",  # Empty string
        "plainaddress",  # Missing @ and domain
        "@missingusername.com",  # Missing username
        "username@.com",  # Missing domain name
        "username@domain..com"  # Consecutive dots
    ]
    for email in invalid_emails:
        with pytest.raises(ValueError):
            send_notification(email=email, order_id="valid123", total=10.0, tracking_number="1234567890")

def test_order_id_invalid_identifier():
    '''Test that invalid order_id formats raise a ValueError'''
    invalid_order_ids = [
        "",  # Empty string
        "!!invalid!!",  # Special characters
        "12345678901234567890123456789012345678901234567890"  # Too long
    ]
    for order_id in invalid_order_ids:
        with pytest.raises(ValueError):
            send_notification(email="valid@example.com", order_id=order_id, total=10.0, tracking_number="1234567890")

def test_total_negative_number():
    '''Test that a negative total raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="valid@example.com", order_id="valid123", total=-10.0, tracking_number="1234567890")

def test_total_zero_value():
    '''Test that a zero total raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="valid@example.com", order_id="valid123", total=0.0, tracking_number="1234567890")

def test_invalid_tracking_number_format():
    '''Test that an invalid tracking number format raises a ValueError'''
    invalid_tracking_numbers = [
        "",  # Empty string
        "12345abcde",  # Alphanumeric
        "1234567890123456789012345678901234567890"  # Too long
    ]
    for tracking_number in invalid_tracking_numbers:
        with pytest.raises(ValueError):
            send_notification(email="valid@example.com", order_id="valid123", total=10.0, tracking_number=tracking_number)

def test_notifications_sent_with_invalid_inputs():
    '''Test that notifications are not sent if inputs are invalid'''
    invalid_inputs = [
        {"email": "", "order_id": "valid123", "total": 10.0, "tracking_number": "1234567890"},  # Invalid email
        {"email": "valid@example.com", "order_id": "", "total": 10.0, "tracking_number": "1234567890"},  # Invalid order_id
        {"email": "valid@example.com", "order_id": "valid123", "total": -10.0, "tracking_number": "1234567890"},  # Invalid total
        {"email": "valid@example.com", "order_id": "valid123", "total": 10.0, "tracking_number": ""}  # Invalid tracking_number
    ]
    for inputs in invalid_inputs:
        with pytest.raises(ValueError):
            send_notification(**inputs)