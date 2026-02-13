import pytest
from src.notifications import validate_email, validate_order_id, validate_total, validate_tracking_number

def test_invalid_email_format():
    '''Test that an invalid email format is rejected'''
    invalid_emails = ["plainaddress", "missing@domain", "@missingusername.com", "user@.com"]
    for email in invalid_emails:
        with pytest.raises(ValueError):
            validate_email(email)

def test_empty_email():
    '''Test that an empty email string is rejected'''
    with pytest.raises(ValueError):
        validate_email("")

def test_order_id_with_special_characters():
    '''Test that order_id with special characters is rejected'''
    invalid_order_ids = ["ORD#123", "123!456", "ORD 789"]
    for order_id in invalid_order_ids:
        with pytest.raises(ValueError):
            validate_order_id(order_id)

def test_order_id_empty_string():
    '''Test that an empty order_id string is rejected'''
    with pytest.raises(ValueError):
        validate_order_id("")

def test_negative_total():
    '''Test that a negative total is rejected'''
    with pytest.raises(ValueError):
        validate_total(-1.0)

def test_zero_total():
    '''Test that a total of zero is rejected'''
    with pytest.raises(ValueError):
        validate_total(0.0)

def test_tracking_number_invalid_format():
    '''Test that a tracking number with invalid format is rejected'''
    invalid_tracking_numbers = ["12345-67890", "TRACKING#123", "TRACKING 123"]
    for tracking_number in invalid_tracking_numbers:
        with pytest.raises(ValueError):
            validate_tracking_number(tracking_number)

def test_empty_tracking_number():
    '''Test that an empty tracking number string is rejected'''
    with pytest.raises(ValueError):
        validate_tracking_number("")