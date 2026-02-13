import pytest
from src.notifications import validate_email, validate_total, validate_tracking_number, validate_business_limits

def test_invalid_email_format():
    '''Test that an invalid email format raises a ValueError'''
    invalid_email = "invalid-email-format"
    with pytest.raises(ValueError):
        validate_email(invalid_email)

def test_empty_email():
    '''Test that an empty email raises a ValueError'''
    empty_email = ""
    with pytest.raises(ValueError):
        validate_email(empty_email)

def test_negative_total():
    '''Test that a negative total raises a ValueError'''
    negative_total = -10.0
    with pytest.raises(ValueError):
        validate_total(negative_total)

def test_zero_total():
    '''Test that a zero total raises a ValueError'''
    zero_total = 0.0
    with pytest.raises(ValueError):
        validate_total(zero_total)

def test_exceeding_business_limit():
    '''Test that a total exceeding business limits raises a ValueError'''
    exceeding_total = 1000000.0  # Assuming the limit is below this
    with pytest.raises(ValueError):
        validate_business_limits(exceeding_total)

def test_valid_tracking_number_format():
    '''Test that an invalid tracking number format raises a ValueError'''
    invalid_tracking_number = "12345-abc"
    with pytest.raises(ValueError):
        validate_tracking_number(invalid_tracking_number)

def test_empty_tracking_number():
    '''Test that an empty tracking number raises a ValueError'''
    empty_tracking_number = ""
    with pytest.raises(ValueError):
        validate_tracking_number(empty_tracking_number)

def test_tracking_number_boundary_condition():
    '''Test that a tracking number just below valid format raises a ValueError'''
    invalid_tracking_number = "12345678901234567890"  # Assuming valid length is less
    with pytest.raises(ValueError):
        validate_tracking_number(invalid_tracking_number)