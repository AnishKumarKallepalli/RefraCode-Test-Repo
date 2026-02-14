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
    '''Test that a negative total is rejected as a positive number'''
    with pytest.raises(ValueError):
        validate_total(-1.00)

def test_zero_total_rejected():
    '''Test that zero total is rejected as a positive number'''
    with pytest.raises(ValueError):
        validate_total(0.00)

def test_invalid_order_id_rejected():
    '''Test that an order_id that is not a string is rejected'''
    with pytest.raises(ValueError):
        validate_order_id(12345)

def test_empty_order_id_rejected():
    '''Test that an empty order_id is rejected as invalid identifier'''
    with pytest.raises(ValueError):
        validate_order_id("")

def test_invalid_tracking_number_format_rejected():
    '''Test that a tracking number with invalid characters is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("TRACKING#123")

def test_empty_tracking_number_rejected():
    '''Test that an empty tracking number is rejected as invalid format'''
    with pytest.raises(ValueError):
        validate_tracking_number("")