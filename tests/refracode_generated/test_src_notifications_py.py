import pytest
from src.notifications import validate_email, validate_total, validate_tracking_number

def test_empty_email_rejected():
    '''Test that an empty email is rejected as invalid format'''
    with pytest.raises(ValueError):
        validate_email("")

def test_invalid_email_format_rejected():
    '''Test that an email without "@" is rejected as invalid format'''
    with pytest.raises(ValueError):
        validate_email("invalidemail.com")

def test_negative_total_rejected():
    '''Test that a negative total is rejected as a non-positive number'''
    with pytest.raises(ValueError):
        validate_total(-1)

def test_zero_total_rejected():
    '''Test that zero total is rejected as a non-positive number'''
    with pytest.raises(ValueError):
        validate_total(0)

def test_extremely_large_total_accepted():
    '''Test that an extremely large positive total is accepted'''
    assert validate_total(1e12) == True

def test_empty_tracking_number_rejected():
    '''Test that an empty tracking number is rejected as invalid format'''
    with pytest.raises(ValueError):
        validate_tracking_number("")

def test_invalid_tracking_number_format_rejected():
    '''Test that a tracking number with invalid characters is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("1234-ABCD-!@#")

def test_tracking_number_too_short_rejected():
    '''Test that a tracking number that is too short is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("123")  # Assuming valid tracking numbers must be longer than 3 characters

def test_tracking_number_too_long_rejected():
    '''Test that a tracking number that is too long is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("12345678901234567890")  # Assuming valid tracking numbers must be shorter than 20 characters