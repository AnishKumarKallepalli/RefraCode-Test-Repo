import pytest
from src.notifications import validate_email, validate_total, validate_tracking_number

def test_empty_email_rejected():
    '''Test that an empty email is rejected as invalid'''
    with pytest.raises(ValueError):
        validate_email("")

def test_invalid_email_format_rejected():
    '''Test that an email without "@" is rejected as invalid'''
    with pytest.raises(ValueError):
        validate_email("invalidemail.com")

def test_negative_total_rejected():
    '''Test that a negative total is rejected as invalid'''
    with pytest.raises(ValueError):
        validate_total(-1)

def test_zero_total_rejected():
    '''Test that a total of zero is rejected as invalid'''
    with pytest.raises(ValueError):
        validate_total(0)

def test_extremely_large_total():
    '''Test that an extremely large total is accepted (boundary condition)'''
    assert validate_total(1e+18) is True

def test_extremely_small_positive_total():
    '''Test that a very small positive total is accepted (boundary condition)'''
    assert validate_total(0.01) is True

def test_empty_tracking_number_rejected():
    '''Test that an empty tracking number is rejected as invalid'''
    with pytest.raises(ValueError):
        validate_tracking_number("")

def test_invalid_tracking_number_format_rejected():
    '''Test that a tracking number with invalid characters is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("TRACK123!@#")

def test_tracking_number_length_boundary():
    '''Test that a tracking number that is too short is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("12345")  # Assuming valid tracking numbers must be longer

def test_tracking_number_length_valid():
    '''Test that a valid length tracking number is accepted'''
    assert validate_tracking_number("TRACK123456") is True  # Assuming this is a valid format