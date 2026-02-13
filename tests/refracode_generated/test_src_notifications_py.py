import pytest
from src.notifications import validate_email, validate_order_id, validate_total, validate_tracking_number

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
        validate_total(-1.0)

def test_zero_total_rejected():
    '''Test that a total of zero is rejected'''
    with pytest.raises(ValueError):
        validate_total(0.0)

def test_empty_order_id_rejected():
    '''Test that an empty order_id is rejected'''
    with pytest.raises(ValueError):
        validate_order_id("")

def test_invalid_order_id_format_rejected():
    '''Test that an order_id with invalid characters is rejected'''
    with pytest.raises(ValueError):
        validate_order_id("order#123")

def test_empty_tracking_number_rejected():
    '''Test that an empty tracking_number is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("")

def test_invalid_tracking_number_format_rejected():
    '''Test that a tracking_number with invalid format is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("TRACKING123@")

def test_large_positive_total_accepted():
    '''Test that a very large positive total is accepted'''
    assert validate_total(1e+10) is None

def test_large_negative_total_rejected():
    '''Test that a very large negative total is rejected'''
    with pytest.raises(ValueError):
        validate_total(-1e+10)