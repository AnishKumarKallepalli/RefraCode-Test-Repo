import pytest
from src.notifications import main_function

def test_main_function_happy_path():
    # Check that the function works correctly with valid inputs.
    result = main_function(notification_type="email", recipient="user@example.com", message="Hello!")
    assert result == "Notification sent successfully"

def test_main_function_invalid_notification_type():
    # Check that the function raises a ValueError for an invalid notification type.
    with pytest.raises(ValueError):
        main_function(notification_type="invalid_type", recipient="user@example.com", message="Hello!")

def test_main_function_empty_recipient():
    # Check that the function raises a ValueError for an empty recipient.
    with pytest.raises(ValueError):
        main_function(notification_type="email", recipient="", message="Hello!")

def test_main_function_empty_message():
    # Check that the function raises a ValueError for an empty message.
    with pytest.raises(ValueError):
        main_function(notification_type="email", recipient="user@example.com", message="")