import pytest
from src.notifications import validate_email, validate_order_id, validate_total, validate_tracking_number

def test_invalid_email_format():
    '''Test that an invalid email format raises a ValueError'''
    invalid_emails = ["plainaddress", "missingatsign.com", "@missingusername.com", "username@.com"]
    for email in invalid_emails:
        with pytest.raises(ValueError):
            validate_email(email)

def test_empty_email():
    '''Test that an empty email raises a ValueError'''
    with pytest.raises(ValueError):
        validate_email("")

def test_null_email():
    '''Test that a None email raises a ValueError'''
    with pytest.raises(ValueError):
        validate_email(None)

def test_invalid_order_id_format():
    '''Test that an invalid order_id format raises a ValueError'''
    invalid_order_ids = ["", "123abc", "order-!@#"]
    for order_id in invalid_order_ids:
        with pytest.raises(ValueError):
            validate_order_id(order_id)

def test_negative_total():
    '''Test that a negative total raises a ValueError'''
    with pytest.raises(ValueError):
        validate_total(-1.0)

def test_zero_total():
    '''Test that a zero total raises a ValueError'''
    with pytest.raises(ValueError):
        validate_total(0.0)

def test_large_negative_total():
    '''Test that a very large negative total raises a ValueError'''
    with pytest.raises(ValueError):
        validate_total(-1e12)

def test_invalid_tracking_number_format():
    '''Test that an invalid tracking number format raises a ValueError'''
    invalid_tracking_numbers = ["", "123456", "TRACK-!@#"]
    for tracking_number in invalid_tracking_numbers:
        with pytest.raises(ValueError):
            validate_tracking_number(tracking_number)

def test_null_tracking_number():
    '''Test that a None tracking number raises a ValueError'''
    with pytest.raises(ValueError):
        validate_tracking_number(None)