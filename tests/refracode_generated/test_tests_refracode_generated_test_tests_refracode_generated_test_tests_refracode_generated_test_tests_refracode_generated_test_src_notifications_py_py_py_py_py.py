import pytest
from src.notifications import validate_email, validate_total, validate_tracking_number

def test_empty_email_rejected():
    '''Test that email cannot be empty'''
    with pytest.raises(ValueError, match="Email must not be empty"):
        validate_email("")

def test_invalid_email_format_rejected():
    '''Test that invalid email formats are rejected'''
    invalid_emails = ["plainaddress", "missing@domain", "@missingusername.com", "username@.com"]
    for email in invalid_emails:
        with pytest.raises(ValueError, match="Email must be valid format"):
            validate_email(email)

def test_negative_total_rejected():
    '''Test that total cannot be negative'''
    with pytest.raises(ValueError, match="Total must be greater than 0"):
        validate_total(-1)

def test_zero_total_rejected():
    '''Test that total cannot be zero'''
    with pytest.raises(ValueError, match="Total must be greater than 0"):
        validate_total(0)

def test_exceeding_business_limits_rejected():
    '''Test that total cannot exceed business limits'''
    business_limit = 10000  # Example business limit
    with pytest.raises(ValueError, match="Total must not exceed business limits"):
        validate_total(business_limit + 1)

def test_empty_tracking_number_rejected():
    '''Test that tracking number cannot be empty'''
    with pytest.raises(ValueError, match="Tracking number must not be empty"):
        validate_tracking_number("")

def test_invalid_tracking_number_format_rejected():
    '''Test that invalid tracking number formats are rejected'''
    invalid_tracking_numbers = ["12345", "ABC-123", "12345678901234567890"]
    for tracking_number in invalid_tracking_numbers:
        with pytest.raises(ValueError, match="Tracking number must be valid format"):
            validate_tracking_number(tracking_number)

def test_boundary_condition_total_limit():
    '''Test that total exactly at business limit is accepted'''
    business_limit = 10000  # Example business limit
    try:
        validate_total(business_limit)
    except ValueError:
        pytest.fail("Total at business limit should not raise an error")