# PaymentProcessing Class
class PaymentProcessing:
    """
    The PaymentProcessing class handles validation and processing of payments using different payment methods.
    
    Attributes:
        available_gateways (list): A list of supported payment gateways such as 'credit_card' and 'paypal'.
    """
    def __init__(self):
        """
        Initializes the PaymentProcessing class with available payment gateways.
        """
        self.available_gateways = ["credit_card", "paypal"]

    def validate_payment_method(self, payment_method, payment_details):
        """
        Validates the selected payment method and its associated details.
        
        Args:
            payment_method (str): The selected payment method (e.g., 'credit_card', 'paypal').
            payment_details (dict): The details required for the payment method (e.g., card number, expiry date).
        
        Returns:
            bool: True if the payment method and details are valid, otherwise raises ValueError.
        
        Raises:
            ValueError: If the payment method is not supported or if the payment details are invalid.
        """
        # Check if the payment method is supported.
        if payment_method not in self.available_gateways:
            raise ValueError("Invalid payment method")

        # Validate credit card details if the selected method is 'credit_card'.
        if payment_method == "credit_card":
            if not self.validate_credit_card(payment_details):
                raise ValueError("Invalid credit card details")

        # Validation passed.
        return True

    def validate_credit_card(self, details):
        """
        Validates the credit card details (e.g., card number, expiry date, CVV).
        
        Args:
            details (dict): A dictionary containing 'card_number', 'expiry_date', and 'cvv'.
        
        Returns:
            bool: True if the card details are valid, False otherwise.
        """
        card_number = details.get("card_number", "")
        expiry_date = details.get("expiry_date", "")
        cvv = details.get("cvv", "")

        # Basic validation: Check if the card number is 16 digits and CVV is 3 digits.
        if len(card_number) != 16 or len(cvv) != 3:
            return False

        # More advanced validations like the Luhn Algorithm for card number can be added here.
        return True

    def process_payment(self, order, payment_method, payment_details):
        """
        Processes the payment for an order, validating the payment method and interacting with the payment gateway.
        
        Args:
            order (dict): The order details, including total amount.
            payment_method (str): The selected payment method.
            payment_details (dict): The details required for the payment method.
        
        Returns:
            str: A message indicating whether the payment was successful or failed.
        """
        try:
            # Validate the payment method and details.
            self.validate_payment_method(payment_method, payment_details)
            
            # Simulate interaction with the payment gateway.
            payment_response = self.mock_payment_gateway(payment_method, payment_details, order["total_amount"])

            # Return the appropriate message based on the payment gateway's response.
            if payment_response["status"] == "success":
                return "Payment successful, Order confirmed"
            else:
                return "Payment failed, please try again"

        except Exception as e:
            # Catch and return any validation or processing errors.
            return f"Error: {str(e)}"

    def mock_payment_gateway(self, method, details, amount):
        """
        Simulates the interaction with a payment gateway for processing payments.
        
        Args:
            method (str): The payment method (e.g., 'credit_card').
            details (dict): The payment details (e.g., card number).
            amount (float): The amount to be charged.
        
        Returns:
            dict: A mock response from the payment gateway, indicating success or failure.
        """
        # Simulate card decline for a specific card number.
        if method == "credit_card" and details["card_number"] == "1111222233334444":
            return {"status": "failure", "message": "Card declined"}

        # Mock a successful transaction.
        return {"status": "success", "transaction_id": "abc123"}