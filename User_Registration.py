class UserRegistration:
    def __init__(self):
        """
        Initializes the UserRegistration class with an empty dictionary to store user data.
        Each entry in the dictionary will map an email to a dictionary containing the user's password and confirmation status.
        """
        self.users = {}

    def register(self, email, password, confirm_password):
        """
        Registers a new user.
        
        This function takes an email, password, and password confirmation as input. It performs a series of checks to ensure the registration 
        is valid:
        - Verifies that the email is in a valid format.
        - Ensures that the password matches the confirmation password.
        - Validates that the password meets the strength requirements.
        - Checks if the email is already registered.
        
        If all checks pass, the user is registered, and their email and password are stored in the `users` dictionary, along with a confirmation 
        status set to False (indicating the user is not yet confirmed). A success message is returned.

        Args:
            email (str): The user's email address.
            password (str): The user's password.
            confirm_password (str): Confirmation of the user's password.
        
        Returns:
            dict: A dictionary containing the result of the registration attempt. 
                  On success, it returns {"success": True, "message": "Registration successful, confirmation email sent"}.
                  On failure, it returns {"success": False, "error": "Specific error message"}.
        """
        if not self.is_valid_email(email):
            return {"success": False, "error": "Invalid email format"}  # If email format is invalid, return an error.
        if password != confirm_password:
            return {"success": False, "error": "Passwords do not match"}  # If passwords don't match, return an error.
        if not self.is_strong_password(password):
            return {"success": False, "error": "Password is not strong enough"}  # If password isn't strong, return an error.
        if email in self.users:
            return {"success": False, "error": "Email already registered"}  # If the email is already registered, return an error.

        # Register the user if all conditions are met and return a success message.
        self.users[email] = {"password": password, "confirmed": False}
        return {"success": True, "message": "Registration successful, confirmation email sent"}

    def is_valid_email(self, email):
        """
        Checks if the provided email is valid based on a simple validation rule.
        This rule only checks that the email contains an '@' symbol and has a '.' in the domain part.

        Args:
            email (str): The email address to be validated.
        
        Returns:
            bool: True if the email is valid, False otherwise.
        """
        if email.count("@") != 1:
            return False
        
        local, domain = email.split("@")

        if not local or not domain:
            return False
        
        if "." not in domain:
            return False
       
        if domain.startswith(".") or domain.endswith("."):
            return False
        
        return True

    def is_strong_password(self, password):
        """
        Checks if the provided password meets the strength requirements.
        A strong password is defined as one that is at least 8 characters long, contains at least one letter, and at least one number.

        Args:
            password (str): The password to be validated.
        
        Returns:
            bool: True if the password is strong, False otherwise.
        """
        return len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isalpha() for c in password)