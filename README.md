# MobileFoodDeliveryApp – Practical Unit Testing Frameworks, Mocking, Stubbing and Fakes

## Overview
This project improves the testing quality of the MobileFoodDeliveryApp using:
- Unit testing (pytest)
- Code coverage analysis
- Test-driven development (TDD)
- Isolation techniques (stubs, mocks, fakes)

## Project Structure

### Application Code
- Favorites_Manager.py
- Order_History.py
- Order_Placement.py
- Payment_Processing.py
- Restaurant_Browsing.py
- User_Registration.py
- Validators.py

### Unit Tests
#### Core test files:
- test_order_placement.py
- test_payment_processing.py
- test_restaurant_browsing.py
- test_order_history.py
- test_user_registration.py
- test_favorites_manager.py

#### Validation & edge cases:
- test_quantity_validation.py
- test_remove_item.py
- test_promo_code.py

### Isolation Tests
- test_email_stub.py → Stub implementation for email validation
- test_payment_mock.py → Mocking payment interactions
- test_payment_fake.py → Fake payment gateway implementation

## Code Coverage

Coverage tool used:
```bash
coverage run -m pytest
coverage report -m
