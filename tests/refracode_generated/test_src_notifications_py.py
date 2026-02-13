import pytest
from src.notifications import validate_email, validate_total, validate_tracking_number

def test_invalid_email_format_empty():
    '''Test that an empty email raises a ValueError'''
    with pytest.raises(ValueError):
        validate_email("")

def test_invalid_email_format_missing_at_symbol():
    '''Test that an email without "@" raises a ValueError'''
    with pytest.raises(ValueError):
        validate_email("testemail.com")

def test_invalid_email_format_missing_domain():
    '''Test that an email without a domain raises a ValueError'''
    with pytest.raises(ValueError):
        validate_email("test@.com")

def test_total_negative_value():
    '''Test that a negative total raises a ValueError'''
    with pytest.raises(ValueError):
        validate_total(-1)

def test_total_zero_value():
    '''Test that a zero total raises a ValueError'''
    with pytest.raises(ValueError):
        validate_total(0)

def test_total_extremely_large_value():
    '''Test that an extremely large total does not raise an error'''
    try:
        validate_total(1e+100)
    except ValueError:
        pytest.fail("validate_total raised ValueError unexpectedly!")

def test_invalid_tracking_number_format_empty():
    '''Test that an empty tracking number raises a ValueError'''
    with pytest.raises(ValueError):
        validate_tracking_number("")

def test_invalid_tracking_number_format_too_short():
    '''Test that a tracking number that is too short raises a ValueError'''
    with pytest.raises(ValueError):
        validate_tracking_number("123")

def test_invalid_tracking_number_format_invalid_characters():
    '''Test that a tracking number with invalid characters raises a ValueError'''
    with pytest.raises(ValueError):
        validate_tracking_number("ABC-1234!@#")