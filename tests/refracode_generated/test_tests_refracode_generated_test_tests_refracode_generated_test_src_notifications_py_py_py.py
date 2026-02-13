import pytest
from src.notifications import validate_email, validate_total, validate_tracking_number

def test_empty_email_rejected():
    '''Test that an empty email is rejected'''
    with pytest.raises(ValueError):
        validate_email("")

def test_invalid_email_format_rejected():
    '''Test that an email with invalid format is rejected'''
    with pytest.raises(ValueError):
        validate_email("invalid-email-format")

def test_total_zero_rejected():
    '''Test that a total of zero is rejected'''
    with pytest.raises(ValueError):
        validate_total(0)

def test_total_negative_rejected():
    '''Test that a negative total is rejected'''
    with pytest.raises(ValueError):
        validate_total(-1)

def test_total_exceeds_business_limits_rejected():
    '''Test that a total exceeding business limits is rejected'''
    with pytest.raises(ValueError):
        validate_total(1000001)  # Assuming 1,000,000 is the business limit

def test_empty_tracking_number_rejected():
    '''Test that an empty tracking number is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("")

def test_invalid_tracking_number_format_rejected():
    '''Test that a tracking number with invalid format is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("123-ABC")  # Assuming valid format is only digits

def test_tracking_number_length_boundary_rejected():
    '''Test that a tracking number that is too short is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("123")  # Assuming valid tracking number must be at least 10 digits

def test_tracking_number_length_boundary_accepted():
    '''Test that a tracking number that is exactly the valid length is accepted'''
    assert validate_tracking_number("1234567890")  # Assuming valid tracking number is 10 digits

def test_total_boundary_condition_accepted():
    '''Test that a total exactly at the business limit is accepted'''
    assert validate_total(1000000)  # Assuming 1,000,000 is the business limit