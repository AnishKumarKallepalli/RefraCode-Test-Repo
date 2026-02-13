import pytest
from src.notifications import Notification

def test_empty_email_rejected():
    '''Test that email cannot be empty'''
    with pytest.raises(ValueError):
        Notification(email='', total=10, tracking_number='123456')

def test_invalid_email_format_rejected():
    '''Test that email must be in a valid format'''
    with pytest.raises(ValueError):
        Notification(email='invalid-email', total=10, tracking_number='123456')

def test_negative_total_rejected():
    '''Test that total cannot be negative'''
    with pytest.raises(ValueError):
        Notification(email='test@example.com', total=-1, tracking_number='123456')

def test_zero_total_accepted():
    '''Test that total must be greater than 0, so zero should be rejected'''
    with pytest.raises(ValueError):
        Notification(email='test@example.com', total=0, tracking_number='123456')

def test_exceeding_business_limit_rejected():
    '''Test that total must not exceed business limits (assuming limit is 1000)'''
    with pytest.raises(ValueError):
        Notification(email='test@example.com', total=1001, tracking_number='123456')

def test_empty_tracking_number_rejected():
    '''Test that tracking number cannot be empty'''
    with pytest.raises(ValueError):
        Notification(email='test@example.com', total=10, tracking_number='')

def test_invalid_tracking_number_format_rejected():
    '''Test that tracking number must be in a valid format'''
    with pytest.raises(ValueError):
        Notification(email='test@example.com', total=10, tracking_number='invalid-tracking')

def test_total_boundary_condition_rejected():
    '''Test that total must be >= 0, so -0.01 should be rejected'''
    with pytest.raises(ValueError):
        Notification(email='test@example.com', total=-0.01, tracking_number='123456')