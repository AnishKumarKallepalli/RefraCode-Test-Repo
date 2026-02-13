import pytest
from src.notifications import validate_email, validate_total, validate_tracking_number

def test_empty_email_rejected():
    '''Test that an empty email is rejected'''
    with pytest.raises(ValueError):
        validate_email("")

def test_invalid_email_format_rejected():
    '''Test that an invalid email format is rejected'''
    with pytest.raises(ValueError):
        validate_email("invalid-email-format")

def test_total_zero_rejected():
    '''Test that a total of zero is rejected'''
    with pytest.raises(ValueError):
        validate_total(0)

def test_total_negative_rejected():
    '''Test that a negative total is rejected'''
    with pytest.raises(ValueError):
        validate_total(-1)

def test_tracking_number_empty_rejected():
    '''Test that an empty tracking number is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("")

def test_invalid_tracking_number_format_rejected():
    '''Test that an invalid tracking number format is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("123-ABC")

def test_total_exceeds_business_limit_rejected():
    '''Test that a total exceeding business limits is rejected'''
    business_limit = 10000  # Example business limit
    with pytest.raises(ValueError):
        validate_total(business_limit + 1)

def test_total_just_below_zero_rejected():
    '''Test that a total just below zero is rejected'''
    with pytest.raises(ValueError):
        validate_total(-0.01)