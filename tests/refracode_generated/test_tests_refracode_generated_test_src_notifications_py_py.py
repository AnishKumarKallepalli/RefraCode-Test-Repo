import pytest
from src.notifications import Notification

def test_invalid_email_format():
    '''Test that an invalid email format raises a ValueError'''
    invalid_email = "invalid-email-format"
    with pytest.raises(ValueError):
        Notification(email=invalid_email, total=100, tracking_number="123456")

def test_empty_email():
    '''Test that an empty email raises a ValueError'''
    empty_email = ""
    with pytest.raises(ValueError):
        Notification(email=empty_email, total=100, tracking_number="123456")

def test_negative_total():
    '''Test that a negative total raises a ValueError'''
    negative_total = -50
    with pytest.raises(ValueError):
        Notification(email="test@example.com", total=negative_total, tracking_number="123456")

def test_zero_total():
    '''Test that a total of zero raises a ValueError'''
    zero_total = 0
    with pytest.raises(ValueError):
        Notification(email="test@example.com", total=zero_total, tracking_number="123456")

def test_exceeding_business_limit():
    '''Test that a total exceeding business limits raises a ValueError'''
    exceeding_total = 1000000  # Assuming the limit is below this value
    with pytest.raises(ValueError):
        Notification(email="test@example.com", total=exceeding_total, tracking_number="123456")

def test_invalid_tracking_number_format():
    '''Test that an invalid tracking number format raises a ValueError'''
    invalid_tracking_number = "123-abc-456"
    with pytest.raises(ValueError):
        Notification(email="test@example.com", total=100, tracking_number=invalid_tracking_number)

def test_empty_tracking_number():
    '''Test that an empty tracking number raises a ValueError'''
    empty_tracking_number = ""
    with pytest.raises(ValueError):
        Notification(email="test@example.com", total=100, tracking_number=empty_tracking_number)

def test_total_just_below_limit():
    '''Test that a total just below the business limit is accepted'''
    just_below_limit = 999999  # Assuming the limit is 1000000
    notification = Notification(email="test@example.com", total=just_below_limit, tracking_number="123456")
    assert notification.total == just_below_limit

def test_total_just_above_limit():
    '''Test that a total just above the business limit raises a ValueError'''
    just_above_limit = 1000001  # Assuming the limit is 1000000
    with pytest.raises(ValueError):
        Notification(email="test@example.com", total=just_above_limit, tracking_number="123456")