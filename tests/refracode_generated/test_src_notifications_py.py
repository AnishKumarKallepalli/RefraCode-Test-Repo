import pytest
from src.notifications import send_notification

def test_invalid_email_format_empty():
    '''Test that an empty email raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="", order_id="12345", total=10.0, tracking_number="TRACK123")

def test_invalid_email_format_missing_at_symbol():
    '''Test that an email without an "@" symbol raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="invalidemail.com", order_id="12345", total=10.0, tracking_number="TRACK123")

def test_invalid_order_id_empty():
    '''Test that an empty order_id raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="test@example.com", order_id="", total=10.0, tracking_number="TRACK123")

def test_invalid_order_id_non_numeric():
    '''Test that a non-numeric order_id raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="test@example.com", order_id="ORDER123", total=10.0, tracking_number="TRACK123")

def test_total_negative():
    '''Test that a negative total raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="test@example.com", order_id="12345", total=-10.0, tracking_number="TRACK123")

def test_total_zero():
    '''Test that a total of zero raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="test@example.com", order_id="12345", total=0.0, tracking_number="TRACK123")

def test_invalid_tracking_number_format_empty():
    '''Test that an empty tracking_number raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="test@example.com", order_id="12345", total=10.0, tracking_number="")

def test_invalid_tracking_number_format_non_alphanumeric():
    '''Test that a tracking_number with special characters raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="test@example.com", order_id="12345", total=10.0, tracking_number="TRACK@123")

def test_notification_not_sent_invalid_email():
    '''Test that notifications are not sent if the email format is invalid'''
    with pytest.raises(ValueError):
        send_notification(email="invalidemail.com", order_id="12345", total=10.0, tracking_number="TRACK123")

def test_notification_not_sent_invalid_order_id():
    '''Test that notifications are not sent if the order_id is invalid'''
    with pytest.raises(ValueError):
        send_notification(email="test@example.com", order_id="ORDER123", total=10.0, tracking_number="TRACK123")

def test_notification_not_sent_negative_total():
    '''Test that notifications are not sent if the total is negative'''
    with pytest.raises(ValueError):
        send_notification(email="test@example.com", order_id="12345", total=-10.0, tracking_number="TRACK123")