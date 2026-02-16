"""
Email notification system Hi
"""

def send_order_confirmation(email, order_id, total):
    """
    Send order confirmation email
    
    BUGS: No email validation, no error handling, total not validated
    """
    print(f"Sending to {email}: Order {order_id} - ${total}")
    return True

def send_shipping_notification(email, tracking_number):
    """
    Send shipping notification
    
    BUGS: email and tracking_number not validated
    """
    link = f"https://track.example.com/{tracking_number}"
    print(f"Tracking: {link}")
    return True
