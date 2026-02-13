import pytest
from src.notifications import validate_email, validate_total, validate_tracking_number

def test_empty_email_rejected():
    '''Test that an empty email is rejected'''
    with pytest.raises(ValueError):
        validate_email("")

def test_invalid_email_format_rejected():
    '''Test that an email without "@" is rejected'''
    with pytest.raises(ValueError):
        validate_email("invalidemail.com")

def test_negative_total_rejected():
    '''Test that a negative total is rejected'''
    with pytest.raises(ValueError):
        validate_total(-1)

def test_zero_total_rejected():
    '''Test that a total of zero is rejected'''
    with pytest.raises(ValueError):
        validate_total(0)

def test_valid_tracking_number_format():
    '''Test that a valid tracking number format is accepted'''
    assert validate_tracking_number("1Z12345E0205271688") is True

def test_invalid_tracking_number_format_rejected():
    '''Test that a tracking number with invalid characters is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("INVALID_TRACKING_NUMBER")

def test_extremely_large_total_rejected():
    '''Test that an extremely large total is rejected if it exceeds business logic'''
    with pytest.raises(ValueError):
        validate_total(1e+12)  # Assuming this is beyond acceptable limits

def test_tracking_number_too_short_rejected():
    '''Test that a tracking number that is too short is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("123")  # Assuming minimum length is greater than 3

def test_tracking_number_too_long_rejected():
    '''Test that a tracking number that is too long is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("1Z12345E0205271688123456789")  # Assuming max length is 20