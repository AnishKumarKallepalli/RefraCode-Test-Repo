import pytest
from src.notifications import send_notification

def test_invalid_email_format():
    '''Test that an invalid email format raises an error'''
    invalid_email = "invalid-email-format"
    order_id = "order123"
    total = 10.0
    tracking_number = "TRACK123"
    with pytest.raises(ValueError):
        send_notification(email=invalid_email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_empty_email():
    '''Test that an empty email raises an error'''
    invalid_email = ""
    order_id = "order123"
    total = 10.0
    tracking_number = "TRACK123"
    with pytest.raises(ValueError):
        send_notification(email=invalid_email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_negative_total():
    '''Test that a negative total raises an error'''
    email = "valid.email@example.com"
    order_id = "order123"
    total = -5.0
    tracking_number = "TRACK123"
    with pytest.raises(ValueError):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_zero_total():
    '''Test that a zero total raises an error'''
    email = "valid.email@example.com"
    order_id = "order123"
    total = 0.0
    tracking_number = "TRACK123"
    with pytest.raises(ValueError):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_invalid_order_id_format():
    '''Test that an invalid order_id format raises an error'''
    email = "valid.email@example.com"
    order_id = ""  # Empty order_id
    total = 10.0
    tracking_number = "TRACK123"
    with pytest.raises(ValueError):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_invalid_tracking_number_format():
    '''Test that an invalid tracking_number format raises an error'''
    email = "valid.email@example.com"
    order_id = "order123"
    total = 10.0
    tracking_number = "12345"  # Invalid format
    with pytest.raises(ValueError):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_notification_sent_with_invalid_email():
    '''Test that notification is not sent if email is invalid'''
    email = "invalid-email-format"
    order_id = "order123"
    total = 10.0
    tracking_number = "TRACK123"
    # Assuming send_notification should not proceed with invalid email
    with pytest.raises(ValueError):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)

def test_notification_sent_with_invalid_order_id_and_total():
    '''Test that notification is not sent if order_id and total are invalid'''
    email = "valid.email@example.com"
    order_id = ""  # Invalid order_id
    total = -10.0  # Invalid total
    tracking_number = "TRACK123"
    with pytest.raises(ValueError):
        send_notification(email=email, order_id=order_id, total=total, tracking_number=tracking_number)