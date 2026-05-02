# Practical Unit Testing Frameworks, Mocking, Stubbing and Fakes

## Overview
This task focuses on improving the testing quality of the MobileFoodDeliveryApp using:
- Unit testing with pytest
- Code coverage analysis (coverage.py)
- Test-Driven Development (TDD)
- Test isolation techniques:
  - Stubs
  - Mocks
  - Fakes
The goal is to improve test reliability, coverage and maintainability.

## Project Structure

### Application Modules
- Favorites_Manager.py
- Order_History.py
- Order_Placement.py
- Payment_Processing.py
- Restaurant_Browsing.py
- User_Registration.py
- Validators.py

### Test Suite

### Core Tests
- test_order_placement.py
- test_payment_processing.py
- test_restaurant_browsing.py
- test_order_history.py
- test_user_registration.py
- test_favorites_manager.py

### Edge Case & Validation Tests
- test_quantity_validation.py
- test_remove_item.py
- test_promo_code.py

### Isolation Techniques Tests
- test_email_stub.py – Stub for email validation
- test_payment_mock.py – Mocking payment interactions
- test_payment_fake.py – Fake payment gateway implementation

## Running Tests

### Run all tests
python3 -m unittest discover -s tests

### Run with verbose output
python3 -m unittest discover -v

### Run a single test file
python3 -m unittest test.test_favorites_manager

## Code Coverage
**Coverage tool used:** coverage.py

### Run coverage analysis
coverage run -m pytest  
coverage report -m  

## Testing Techniques Used
**Stub**: Used to replace external dependencies with fixed responses (e.g., email validation).  
**Mock**: Used to simulate external services and verify interactions (e.g., payment processing calls).  
**Fake**: Used as a simplified working implementation of external systems (e.g., payment gateway simulation).  

## Notes
- Tests are designed to cover normal cases, edge cases and failure scenarios.
- Focus is on improving both coverage and test quality, not just quantity.
- All changes were validated using automated test runs and coverage reports.
