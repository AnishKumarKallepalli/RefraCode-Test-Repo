import pytest
from src.notifications import validate_email, validate_total, validate_tracking_number

def test_empty_email_rejected():
    '''Test that email must not be empty'''
    with pytest.raises(ValueError):
        validate_email("")

def test_invalid_email_format():
    '''Test that invalid email formats are rejected'''
    invalid_emails = ["plainaddress", "@missingusername.com", "username@.com"]
    for email in invalid_emails:
        with pytest.raises(ValueError):
            validate_email(email)

def test_total_zero_rejected():
    '''Test that total must be greater than 0'''
    with pytest.raises(ValueError):
        validate_total(0)

def test_total_negative_rejected():
    '''Test that total must not be negative'''
    with pytest.raises(ValueError):
        validate_total(-1)

def test_total_exceeds_business_limits():
    '''Test that total must not exceed business limits'''
    business_limit = 10000  # Example business limit
    with pytest.raises(ValueError):
        validate_total(business_limit + 1)

def test_empty_tracking_number_rejected():
    '''Test that tracking number must not be empty'''
    with pytest.raises(ValueError):
        validate_tracking_number("")

def test_invalid_tracking_number_format():
    '''Test that invalid tracking number formats are rejected'''
    invalid_tracking_numbers = ["12345", "ABC-123", "TRACKING#NUMBER"]
    for tracking_number in invalid_tracking_numbers:
        with pytest.raises(ValueError):
            validate_tracking_number(tracking_number)

def test_tracking_number_length_boundary():
    '''Test that tracking number must meet length requirements'''
    valid_tracking_number = "TRACK123456"
    invalid_length_tracking_number = "T" * 21  # Assuming max length is 20
    with pytest.raises(ValueError):
        validate_tracking_number(invalid_length_tracking_number)