import re

# Valid tracking number: uppercase alphanumeric, minimum 4 characters
_TRACKING_PATTERN = re.compile(r'^[A-Z0-9]{4,}$')
# Basic RFC-compliant email pattern
_EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$')


def _validate_email(email: str) -> None:
    if not email or not _EMAIL_PATTERN.match(email):
        raise ValueError(f"Invalid email address: {email!r}")


def _validate_tracking_number(tracking_number: str) -> None:
    if not tracking_number or not tracking_number.strip():
        raise ValueError("Tracking number cannot be empty")
    if not _TRACKING_PATTERN.match(tracking_number.upper()):
        raise ValueError(
            f"Invalid tracking number format: {tracking_number!r}. "
            "Must be at least 4 alphanumeric characters."
        )


def send_order_confirmation(order_id: str, email: str, total: float) -> bool:
    """
    Send an order confirmation notification.

    Args:
        order_id: Unique order identifier.
        email:    Recipient email address (must be a valid format).
        total:    Order total in dollars (must be > 0).

    Returns:
        True on success.

    Raises:
        ValueError: If email is invalid or total is not positive.
    """
    _validate_email(email)

    if total <= 0:
        raise ValueError(
            f"Order total must be greater than zero, got {total}"
        )

    print(f"Sending to {email}: Order {order_id} - ${total}")
    return True


def send_shipping_notification(tracking_number: str, email: str) -> bool:
    """
    Send a shipping notification with a tracking link.

    Args:
        tracking_number: Carrier tracking number (>=4 alphanumeric chars).
        email:           Recipient email address (must be a valid format).

    Returns:
        True on success.

    Raises:
        ValueError: If tracking number or email is invalid.
    """
    _validate_tracking_number(tracking_number)
    _validate_email(email)

    print(f"Tracking: https://track.example.com/{tracking_number}")
    return True