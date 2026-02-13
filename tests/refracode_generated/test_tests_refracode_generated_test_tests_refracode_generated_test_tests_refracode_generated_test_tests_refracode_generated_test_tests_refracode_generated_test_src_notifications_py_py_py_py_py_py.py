import pytest
from src.notifications import Notification

def test_empty_email_rejected():
    '''Test that an empty email is rejected'''
    with pytest.raises(ValueError, match="Email must not be empty"):
        Notification(email="", total=10, tracking_number="123456")

def test_invalid_email_format_rejected():
    '''Test that an invalid email format is rejected'''
    with pytest.raises(ValueError, match="Email must be valid format"):
        Notification(email="invalidemail", total=10, tracking_number="123456")

def test_total_zero_rejected():
    '''Test that total must be greater than 0'''
    with pytest.raises(ValueError, match="Total must be greater than 0"):
        Notification(email="test@example.com", total=0, tracking_number="123456")

def test_total_negative_rejected():
    '''Test that total cannot be negative'''
    with pytest.raises(ValueError, match="Total must not be negative"):
        Notification(email="test@example.com", total=-5, tracking_number="123456")

def test_empty_tracking_number_rejected():
    '''Test that an empty tracking number is rejected'''
    with pytest.raises(ValueError, match="Tracking number must not be empty"):
        Notification(email="test@example.com", total=10, tracking_number="")

def test_invalid_tracking_number_format_rejected():
    '''Test that an invalid tracking number format is rejected'''
    with pytest.raises(ValueError, match="Tracking number must be valid format"):
        Notification(email="test@example.com", total=10, tracking_number="abc123")

def test_total_exceeds_business_limits_rejected():
    '''Test that total must not exceed business limits'''
    with pytest.raises(ValueError, match="Total must not exceed business limits"):
        Notification(email="test@example.com", total=1000000, tracking_number="123456")

def test_total_boundary_condition_zero():
    '''Test that total must be >= 0'''
    notification = Notification(email="test@example.com", total=0, tracking_number="123456")
    assert notification.total == 0

def test_total_boundary_condition_positive():
    '''Test that total just above 0 is accepted'''
    notification = Notification(email="test@example.com", total=0.01, tracking_number="123456")
    assert notification.total == 0.01

def test_tracking_number_boundary_condition():
    '''Test that tracking number just below valid length is rejected'''
    with pytest.raises(ValueError, match="Tracking number must be valid format"):
        Notification(email="test@example.com", total=10, tracking_number="12345")  # Assuming valid length is > 5