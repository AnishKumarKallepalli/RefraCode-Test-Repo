import pytest
from src.notifications import send_notification

def test_invalid_email_format_empty():
    '''Test that an empty email raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="", order_id="12345", total=10.0, tracking_number="TRACK123")

def test_invalid_email_format_missing_at_symbol():
    '''Test that an email missing the "@" symbol raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="invalidemail.com", order_id="12345", total=10.0, tracking_number="TRACK123")

def test_invalid_email_format_missing_domain():
    '''Test that an email missing the domain raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="invalidemail@", order_id="12345", total=10.0, tracking_number="TRACK123")

def test_order_id_invalid_format_empty():
    '''Test that an empty order_id raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="valid@example.com", order_id="", total=10.0, tracking_number="TRACK123")

def test_order_id_invalid_format_special_characters():
    '''Test that an order_id with special characters raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="valid@example.com", order_id="!@#$%^", total=10.0, tracking_number="TRACK123")

def test_total_negative_number():
    '''Test that a negative total raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="valid@example.com", order_id="12345", total=-10.0, tracking_number="TRACK123")

def test_total_zero():
    '''Test that a total of zero raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="valid@example.com", order_id="12345", total=0.0, tracking_number="TRACK123")

def test_tracking_number_invalid_format_empty():
    '''Test that an empty tracking_number raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="valid@example.com", order_id="12345", total=10.0, tracking_number="")

def test_tracking_number_invalid_format_missing_prefix():
    '''Test that a tracking_number without the required prefix raises a ValueError'''
    with pytest.raises(ValueError):
        send_notification(email="valid@example.com", order_id="12345", total=10.0, tracking_number="123456")

def test_notification_sent_with_invalid_email():
    '''Test that notification is not sent if email is invalid'''
    with pytest.raises(ValueError):
        send_notification(email="invalidemail.com", order_id="12345", total=10.0, tracking_number="TRACK123")

def test_notification_sent_with_invalid_order_id():
    '''Test that notification is not sent if order_id is invalid'''
    with pytest.raises(ValueError):
        send_notification(email="valid@example.com", order_id="!@#$%^", total=10.0, tracking_number="TRACK123")