from src.notifications import send_order_confirmation, send_shipping_notification

def test_send_order_confirmation_invalid_email_format():
    # Validates that an invalid email format raises an error
    assert not send_order_confirmation(email='not-an-email', order_id='12345', total=100.0)

def test_send_order_confirmation_empty_email():
    # Validates that an empty email raises an error
    assert not send_order_confirmation(email='', order_id='12345', total=100.0)

def test_send_order_confirmation_negative_total():
    # Validates that a negative total raises an error
    assert not send_order_confirmation(email='test@example.com', order_id='12345', total=-50.0)

def test_send_order_confirmation_zero_total():
    # Validates that a total of zero raises an error
    assert not send_order_confirmation(email='test@example.com', order_id='12345', total=0.0)

def test_send_shipping_notification_invalid_tracking_number_format():
    # Validates that an invalid tracking number format raises an error
    assert not send_shipping_notification(email='test@example.com', tracking_number='invalid-tracking')

def test_send_shipping_notification_empty_tracking_number():
    # Validates that an empty tracking number raises an error
    assert not send_shipping_notification(email='test@example.com', tracking_number='')