from src.notifications import send_order_confirmation, send_shipping_notification

def test_send_order_confirmation_invalid_email_format():
    # Validate that sending an order confirmation with an invalid email format fails
    assert not send_order_confirmation(order_id='12345', email='not-an-email', total=10.0)

def test_send_order_confirmation_empty_email():
    # Validate that sending an order confirmation with an empty email fails
    assert not send_order_confirmation(order_id='12345', email='', total=10.0)

def test_send_order_confirmation_total_zero():
    # Validate that sending an order confirmation with total equal to zero fails
    assert not send_order_confirmation(order_id='12345', email='test@example.com', total=0.0)

def test_send_order_confirmation_total_negative():
    # Validate that sending an order confirmation with a negative total fails
    assert not send_order_confirmation(order_id='12345', email='test@example.com', total=-10.0)

def test_send_shipping_notification_tracking_number_too_short():
    # Validate that sending a shipping notification with a tracking number shorter than 4 characters fails
    assert not send_shipping_notification(tracking_number='123', email='test@example.com')

def test_send_shipping_notification_empty_tracking_number():
    # Validate that sending a shipping notification with an empty tracking number fails
    assert not send_shipping_notification(tracking_number='', email='test@example.com')

def test_send_shipping_notification_invalid_email_format():
    # Validate that sending a shipping notification with an invalid email format fails
    assert not send_shipping_notification(tracking_number='TRACK123', email='not-an-email')

def test_send_shipping_notification_empty_email():
    # Validate that sending a shipping notification with an empty email fails
    assert not send_shipping_notification(tracking_number='TRACK123', email='')