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

def test_order_id_with_special_characters_rejected():
    '''Test that an order_id with special characters is rejected'''
    with pytest.raises(ValueError):
        validate_order_id("order@123")

def test_tracking_number_with_invalid_format_rejected():
    '''Test that a tracking number that is too short is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("123")

def test_tracking_number_with_invalid_characters_rejected():
    '''Test that a tracking number with invalid characters is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("TRACK-123-ABC!")