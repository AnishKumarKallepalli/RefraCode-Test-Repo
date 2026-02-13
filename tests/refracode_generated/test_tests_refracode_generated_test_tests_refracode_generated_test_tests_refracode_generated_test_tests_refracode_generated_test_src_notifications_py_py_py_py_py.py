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
    '''Test that a total less than or equal to 0 is rejected'''
    with pytest.raises(ValueError):
        validate_total(-1)

def test_zero_total_rejected():
    '''Test that a total of 0 is rejected'''
    with pytest.raises(ValueError):
        validate_total(0)

def test_exceeding_business_limit_rejected():
    '''Test that a total exceeding business limits is rejected'''
    with pytest.raises(ValueError):
        validate_total(1000001)  # Assuming 1000000 is the business limit

def test_empty_tracking_number_rejected():
    '''Test that an empty tracking number is rejected as invalid format'''
    with pytest.raises(ValueError):
        validate_tracking_number("")

def test_invalid_tracking_number_format_rejected():
    '''Test that a tracking number with invalid characters is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("TRACK#123")

def test_email_with_invalid_domain_rejected():
    '''Test that an email with an invalid domain format is rejected'''
    with pytest.raises(ValueError):
        validate_email("user@invalid_domain")

def test_total_just_below_zero_rejected():
    '''Test that a total just below zero is rejected'''
    with pytest.raises(ValueError):
        validate_total(-0.01)

def test_tracking_number_too_short_rejected():
    '''Test that a tracking number that is too short is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("123")  # Assuming minimum length is greater than 3

def test_tracking_number_too_long_rejected():
    '''Test that a tracking number that is too long is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("T" * 21)  # Assuming maximum length is 20