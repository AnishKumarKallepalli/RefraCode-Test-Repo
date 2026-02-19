import pytest
from src.notifications import send_order_confirmation, send_shipping_notification

@pytest.mark.parametrize("order_id, email, total", [
    ('123', None, 10.0),  # email is None
])
def test_send_order_confirmation_none_email_raises_value_error(order_id, email, total):
    with pytest.raises(ValueError):  # checks that ValueError is raised for None email
        send_order_confirmation(order_id=order_id, email=email, total=total)

@pytest.mark.parametrize("order_id, email, total", [
    ('123', '', 10.0),  # email is empty string
])
def test_send_order_confirmation_empty_email_raises_value_error(order_id, email, total):
    with pytest.raises(ValueError):  # checks that ValueError is raised for empty email
        send_order_confirmation(order_id=order_id, email=email, total=total)

@pytest.mark.parametrize("order_id, email, total", [
    ('123', 'not-an-email', 10.0),  # email missing @ symbol
])
def test_send_order_confirmation_invalid_email_format_raises_value_error(order_id, email, total):
    with pytest.raises(ValueError):  # checks that ValueError is raised for invalid email format
        send_order_confirmation(order_id=order_id, email=email, total=total)

def test_send_order_confirmation_happy_path():
    assert send_order_confirmation(order_id='ORD001', email='user@example.com', total=99.99)  # checks successful execution

@pytest.mark.parametrize("order_id, email, total", [
    ('123', 'user@example.com', 0.0),  # total is zero
])
def test_send_order_confirmation_zero_total_raises_value_error(order_id, email, total):
    with pytest.raises(ValueError):  # checks that ValueError is raised for zero total
        send_order_confirmation(order_id=order_id, email=email, total=total)

@pytest.mark.parametrize("order_id, email, total", [
    ('123', 'user@example.com', -1.0),  # total is negative
])
def test_send_order_confirmation_negative_total_raises_value_error(order_id, email, total):
    with pytest.raises(ValueError):  # checks that ValueError is raised for negative total
        send_order_confirmation(order_id=order_id, email=email, total=total)

def test_send_order_confirmation_positive_total_happy_path():
    assert send_order_confirmation(order_id='123', email='user@example.com', total=1.0)  # checks successful execution

@pytest.mark.parametrize("tracking_number, email", [
    (None, 'user@example.com'),  # tracking_number is None
])
def test_send_shipping_notification_none_tracking_number_raises_value_error(tracking_number, email):
    with pytest.raises(ValueError):  # checks that ValueError is raised for None tracking number
        send_shipping_notification(tracking_number=tracking_number, email=email)

@pytest.mark.parametrize("tracking_number, email", [
    ('', 'user@example.com'),  # tracking_number is empty string
])
def test_send_shipping_notification_empty_tracking_number_raises_value_error(tracking_number, email):
    with pytest.raises(ValueError):  # checks that ValueError is raised for empty tracking number
        send_shipping_notification(tracking_number=tracking_number, email=email)

@pytest.mark.parametrize("tracking_number, email", [
    ('123', 'user@example.com'),  # tracking_number has invalid format
])
def test_send_shipping_notification_invalid_tracking_number_format_raises_value_error(tracking_number, email):
    with pytest.raises(ValueError):  # checks that ValueError is raised for invalid tracking number format
        send_shipping_notification(tracking_number=tracking_number, email=email)

def test_send_shipping_notification_happy_path():
    assert send_shipping_notification(tracking_number='TRACK123', email='user@example.com')  # checks successful execution

@pytest.mark.parametrize("tracking_number, email", [
    ('TRACK123', None),  # email is None
])
def test_send_shipping_notification_none_email_raises_value_error(tracking_number, email):
    with pytest.raises(ValueError):  # checks that ValueError is raised for None email
        send_shipping_notification(tracking_number=tracking_number, email=email)

@pytest.mark.parametrize("tracking_number, email", [
    ('TRACK123', ''),  # email is empty string
])
def test_send_shipping_notification_empty_email_raises_value_error(tracking_number, email):
    with pytest.raises(ValueError):  # checks that ValueError is raised for empty email
        send_shipping_notification(tracking_number=tracking_number, email=email)

@pytest.mark.parametrize("tracking_number, email", [
    ('TRACK123', 'not-an-email'),  # email missing @ symbol
])
def test_send_shipping_notification_invalid_email_format_raises_value_error(tracking_number, email):
    with pytest.raises(ValueError):  # checks that ValueError is raised for invalid email format
        send_shipping_notification(tracking_number=tracking_number, email=email)