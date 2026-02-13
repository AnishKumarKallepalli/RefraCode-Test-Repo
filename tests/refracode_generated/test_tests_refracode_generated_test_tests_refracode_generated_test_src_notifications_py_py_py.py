import pytest
from src.notifications import validate_email, validate_total, validate_tracking_number

def test_invalid_email_format():
    '''Test that an invalid email format is rejected'''
    invalid_emails = ["plainaddress", "missing@domain", "user@.com", "@missingusername.com"]
    for email in invalid_emails:
        with pytest.raises(ValueError):
            validate_email(email)

def test_zero_total_rejected():
    '''Test that total must be greater than 0'''
    with pytest.raises(ValueError):
        validate_total(0)

def test_negative_total_rejected():
    '''Test that total cannot be negative'''
    with pytest.raises(ValueError):
        validate_total(-1)

def test_exceeding_business_limit():
    '''Test that total exceeding business limits is rejected'''
    exceeding_total = 1000000  # Assuming the business limit is less than this
    with pytest.raises(ValueError):
        validate_total(exceeding_total)

def test_invalid_tracking_number_format():
    '''Test that an invalid tracking number format is rejected'''
    invalid_tracking_numbers = ["12345", "TRACK-1234567", "TRACK12345678"]
    for tracking_number in invalid_tracking_numbers:
        with pytest.raises(ValueError):
            validate_tracking_number(tracking_number)

def test_empty_email_rejected():
    '''Test that an empty email is rejected'''
    with pytest.raises(ValueError):
        validate_email("")

def test_boundary_total_limit():
    '''Test that total at the business limit is accepted'''
    valid_total = 999999  # Assuming the business limit is 1000000
    assert validate_total(valid_total) is None  # Should not raise an error

def test_tracking_number_too_short():
    '''Test that a tracking number that is too short is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("TRK123")  # Assuming valid tracking numbers are longer

def test_tracking_number_too_long():
    '''Test that a tracking number that is too long is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("TRACKINGNUMBER1234567890")  # Assuming valid tracking numbers are shorter

def test_null_total_rejected():
    '''Test that a null total is rejected'''
    with pytest.raises(ValueError):
        validate_total(None)