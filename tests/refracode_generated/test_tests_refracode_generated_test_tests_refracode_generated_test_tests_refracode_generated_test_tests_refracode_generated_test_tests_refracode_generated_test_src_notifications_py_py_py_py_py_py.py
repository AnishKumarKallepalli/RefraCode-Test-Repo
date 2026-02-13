import pytest
from src.notifications import validate_email, validate_total, validate_tracking_number

def test_empty_email_rejected():
    '''Test that empty email is rejected'''
    with pytest.raises(ValueError, match="Email must not be empty"):
        validate_email("")

def test_invalid_email_format_rejected():
    '''Test that invalid email format is rejected'''
    with pytest.raises(ValueError, match="Email must be valid format"):
        validate_email("invalid-email")

def test_total_zero_rejected():
    '''Test that total must be greater than 0'''
    with pytest.raises(ValueError, match="Total must be greater than 0"):
        validate_total(0)

def test_total_negative_rejected():
    '''Test that total cannot be negative'''
    with pytest.raises(ValueError, match="Total must not be negative"):
        validate_total(-1)

def test_tracking_number_empty_rejected():
    '''Test that empty tracking number is rejected'''
    with pytest.raises(ValueError, match="Tracking number must not be empty"):
        validate_tracking_number("")

def test_invalid_tracking_number_format_rejected():
    '''Test that invalid tracking number format is rejected'''
    with pytest.raises(ValueError, match="Tracking number must be valid format"):
        validate_tracking_number("123-abc")

def test_total_exceeds_business_limits_rejected():
    '''Test that total exceeding business limits is rejected'''
    business_limit = 10000  # Example business limit
    with pytest.raises(ValueError, match="Total must not exceed business limits"):
        validate_total(business_limit + 1)

def test_total_boundary_condition_rejected():
    '''Test that total exactly at the business limit is accepted'''
    business_limit = 10000  # Example business limit
    assert validate_total(business_limit) is None

def test_total_boundary_condition_just_below_limit():
    '''Test that total just below the business limit is accepted'''
    business_limit = 10000  # Example business limit
    assert validate_total(business_limit - 1) is None

def test_total_boundary_condition_just_above_limit_rejected():
    '''Test that total just above the business limit is rejected'''
    business_limit = 10000  # Example business limit
    with pytest.raises(ValueError, match="Total must not exceed business limits"):
        validate_total(business_limit + 0.01)