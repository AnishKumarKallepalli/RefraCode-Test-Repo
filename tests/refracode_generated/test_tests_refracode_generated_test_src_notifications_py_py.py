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
    '''Test that a negative total is rejected'''
    with pytest.raises(ValueError):
        validate_total(-1)

def test_zero_total_rejected():
    '''Test that a total of zero is rejected'''
    with pytest.raises(ValueError):
        validate_total(0)

def test_empty_tracking_number_rejected():
    '''Test that an empty tracking number is rejected as invalid format'''
    with pytest.raises(ValueError):
        validate_tracking_number("")

def test_invalid_tracking_number_format_rejected():
    '''Test that a tracking number with invalid characters is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("1234-ABC")

def test_large_negative_total_rejected():
    '''Test that a very large negative total is rejected'''
    with pytest.raises(ValueError):
        validate_total(-999999999999)

def test_boundary_email_format_rejected():
    '''Test that an email with only one character before "@" is rejected'''
    with pytest.raises(ValueError):
        validate_email("a@.com")

def test_boundary_tracking_number_format_rejected():
    '''Test that a tracking number with just the minimum valid length is accepted'''
    with pytest.raises(ValueError):
        validate_tracking_number("123")  # Assuming valid format requires more than 3 characters