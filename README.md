# More Advanced Testing
A Python-based Mobile Food Delivery application built for a Software Testing project.  
The project focuses on improving software quality using static testing, dynamic testing and TDD (Test-Driven Development).  

## Features
- User registration and authentication
- Restaurant browsing
- Order placement and checkout
- Payment processing simulation
- Cart management (add/remove items)
- Order history tracking
- Favorite restaurants system
- Promo code discounts

## Testing Overview
This project includes both static and dynamic testing:  
### Static Testing
- Manual code review
- Pylint for code quality
- Bandit for security analysis
### Dynamic Testing
- Python unittest framework used
- Existing and custom test cases
- Edge case testing (invalid inputs, empty data, etc.)

## More Advanced Testing

### Pylint (Code Quality Analysis)
Pylint is used to check code quality, structure and maintainability.  
**Run Pylint:** pylint *.py  
**Or for specific files:** pylint main.py  

It detects:
- Style problems
- Naming issues
- Unused code
- Design problems

### Bandit (Security Analysis)
Bandit is used to detect security vulnerabilities in the code.  
**Run Bandit:** bandit -r .  

It detects:
- Hardcoded secrets
- Unsafe file handling
- Common security risks

## Test-Driven Development (TDD)
New features were developed using the Red -> Green -> Refactor cycle:
Implemented features:  
- Order quantity validation
- Favorites system
- Cart item removal
- Order history
- Promo code system

Each feature includes:  
- Unit tests written first
- Minimal implementation to pass tests
- Refactoring for cleaner design

## Project Structure
- main.py  
- Order_Placement.py  
- Payment_Processing.py  
- Restaurant_Browsing.py  
- User_Registration.py  
- Order_History.py  
- Favorites_Manager.py  
- users.json  

### Tests
- test_quantity_validation.py  
- test_remove_item.py  
- test_favorites_manager.py  
- test_order_history.py  
- test_promo_code.py  

## Technologies Used
- Python 3
- unittest
- Pylint
- Bandit
- Git & GitHub

## How to Run

### Run the application:
python main.py

### Run tests:
python -m unittest discover

## Summary
This project shows how software quality can be improved using:
- Static analysis before execution
- Dynamic testing during execution
- Test-driven development for new features
- Iterative Agile-style improvement
