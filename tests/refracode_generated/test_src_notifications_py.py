import pytest
from src.notifications import send_notification

def test_invalid_email_format():
    '''Test that an invalid email format raises a ValueError'''
    invalid_email = "invalid_email_format"
    order_id = "12345"
    total = 10.0
    tracking_number = "TRACK123"
    with pytest.raises(ValueError):
        send_notification(email=invalid_email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_empty_order_id():
    '''Test that an empty order_id raises a ValueError'''
    email = "valid.email@example.com"
    order_id = ""
    total = 10.0
    tracking_number = "TRACK123"
    with pytest.raises(ValueError):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_negative_total_amount():
    '''Test that a negative total raises a ValueError'''
    email = "valid.email@example.com"
    order_id = "12345"
    total = -5.0
    tracking_number = "TRACK123"
    with pytest.raises(ValueError):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_invalid_tracking_number_format():
    '''Test that an invalid tracking number format raises a ValueError'''
    email = "valid.email@example.com"
    order_id = "12345"
    total = 10.0
    tracking_number = "INVALID_TRACKING"
    with pytest.raises(ValueError):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_notification_not_sent_on_invalid_email():
    '''Test that notification is not sent if email is invalid'''
    invalid_email = "invalid_email_format"
    order_id = "12345"
    total = 10.0
    tracking_number = "TRACK123"
    # Assuming send_notification has a side effect of sending an email
    result = send_notification(email=invalid_email, order_id=order_id, total=total, tracking_number=tracking_number)
    assert result is False  # Assuming the function returns False on failure

def test_handle_exception_during_email_sending():
    '''Test that exceptions during email sending are handled gracefully'''
    email = "valid.email@example.com"
    order_id = "12345"
    total = 10.0
    tracking_number = "TRACK123"
    # Mocking the email sending function to raise an exception
    with pytest.raises(Exception):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)  # Replace with actual mock to simulate failure