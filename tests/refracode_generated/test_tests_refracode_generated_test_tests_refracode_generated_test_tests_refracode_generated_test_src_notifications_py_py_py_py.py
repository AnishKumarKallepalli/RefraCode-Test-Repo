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

def test_zero_total_rejected():
    '''Test that total cannot be zero'''
    with pytest.raises(ValueError):
        validate_total(0)

def test_negative_total_rejected():
    '''Test that total cannot be negative'''
    with pytest.raises(ValueError):
        validate_total(-100)

def test_exceeding_business_limit_rejected():
    '''Test that total exceeding business limits is rejected'''
    with pytest.raises(ValueError):
        validate_total(1000000)  # Assuming 999999 is the limit

def test_empty_tracking_number_rejected():
    '''Test that an empty tracking number is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("")

def test_invalid_tracking_number_format_rejected():
    '''Test that an invalid tracking number format is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("123-abc")  # Assuming valid format is only digits

def test_total_just_below_limit_rejected():
    '''Test that total just below the limit is accepted'''
    assert validate_total(999998) == True  # Assuming 999999 is the limit

def test_total_just_above_limit_rejected():
    '''Test that total just above the limit is rejected'''
    with pytest.raises(ValueError):
        validate_total(1000000)  # Assuming 999999 is the limit

def test_null_email_rejected():
    '''Test that a null email is rejected'''
    with pytest.raises(ValueError):
        validate_email(None)

def test_null_total_rejected():
    '''Test that a null total is rejected'''
    with pytest.raises(ValueError):
        validate_total(None)

def test_null_tracking_number_rejected():
    '''Test that a null tracking number is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number(None)