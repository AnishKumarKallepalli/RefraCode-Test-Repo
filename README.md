# E-Commerce Platform - Test Repository

A realistic e-commerce backend system for testing RefraCode AI-powered QA.

## Features

- User authentication & authorization
- Payment processing
- Shopping cart & checkout
- Inventory management
- Order processing
- Email notifications

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from src.auth import UserAuth
from src.payment import PaymentProcessor
from src.cart import ShoppingCart

# Initialize
auth = UserAuth()
payment = PaymentProcessor(merchant_id="TEST", api_key="key123")
cart = ShoppingCart(user_id=1)

# Use the system
user_id = auth.register_user("john", "john@example.com", "pass123")
cart.add_item("PROD-001", quantity=2, price=29.99)
total = cart.calculate_total()
```

## Testing

This repository intentionally contains bugs to test RefraCode's ability to detect:
- Input validation issues
- Business logic errors
- Security vulnerabilities
- Edge case handling

## License

MIT
