import pytest
from src.notifications import validate_email, validate_order_id, validate_total, validate_tracking_number

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
        validate_total(-10.0)

def test_zero_total_rejected():
    '''Test that zero total is rejected as a non-positive number'''
    with pytest.raises(ValueError):
        validate_total(0.0)

def test_order_id_with_special_characters_rejected():
    '''Test that an order_id with special characters is rejected as invalid identifier'''
    with pytest.raises(ValueError):
        validate_order_id("ORD#123")

def test_tracking_number_with_invalid_format_rejected():
    '''Test that a tracking number that is too short is rejected as invalid format'''
    with pytest.raises(ValueError):
        validate_tracking_number("123")

def test_large_positive_total():
    '''Test that a very large positive total is accepted'''
    assert validate_total(1e+10) is None

def test_order_id_with_empty_string_rejected():
    '''Test that an empty string as order_id is rejected as invalid identifier'''
    with pytest.raises(ValueError):
        validate_order_id("")

def test_tracking_number_with_invalid_length_rejected():
    '''Test that a tracking number that is too long is rejected as invalid format'''
    with pytest.raises(ValueError):
        validate_tracking_number("A" * 21)  # Assuming valid tracking number length is <= 20