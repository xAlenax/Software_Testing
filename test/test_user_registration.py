# Unit tests for UserRegistration class
import unittest
from User_Registration import UserRegistration

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment by creating an instance of the UserRegistration class.
        This instance will be used across all test cases.
        """
        self.registration = UserRegistration()

    def test_successful_registration(self):
        """
        Test case for successful user registration.
        It verifies that a valid email and matching strong password results in successful registration.
        """
        result = self.registration.register("user@example.com", "Password123", "Password123")
        self.assertTrue(result['success'])  # Ensures that registration is successful.
        self.assertEqual(result['message'], "Registration successful, confirmation email sent")  # Checks the success message.

    def test_invalid_email(self):
        """
        Test case for invalid email format.
        It verifies that attempting to register with an incorrectly formatted email results in an error.
        """
        result = self.registration.register("userexample.com", "Password123", "Password123")
        self.assertFalse(result['success'])  # Ensures registration fails due to invalid email.
        self.assertEqual(result['error'], "Invalid email format")  # Checks the specific error message.

    def test_password_mismatch(self):
        """
        Test case for password mismatch.
        It verifies that when the password and confirmation password do not match, registration fails.
        """
        result = self.registration.register("user@example.com", "Password123", "Password321")
        self.assertFalse(result['success'])  # Ensures registration fails due to password mismatch.
        self.assertEqual(result['error'], "Passwords do not match")  # Checks the specific error message.

    def test_weak_password(self):
        """
        Test case for weak password.
        It verifies that a password not meeting the strength requirements results in an error.
        """
        result = self.registration.register("user@example.com", "pass", "pass")
        self.assertFalse(result['success'])  # Ensures registration fails due to a weak password.
        self.assertEqual(result['error'], "Password is not strong enough")  # Checks the specific error message.

    def test_email_already_registered(self):
        """
        Test case for duplicate email registration.
        It verifies that attempting to register an email that has already been registered results in an error.
        """
        self.registration.register("user@example.com", "Password123", "Password123")  # Register a user.
        result = self.registration.register("user@example.com", "Password123", "Password123")
        self.assertFalse(result['success'])  # Ensures registration fails due to the email already being registered.
        self.assertEqual(result['error'], "Email already registered")  # Checks the specific error message.

    def test_is_valid_email(self):
        """
        Test various valid and invalid email formats.
        """
        # Valid
        self.assertTrue(self.registration.is_valid_email("user@example.com"))

        # Invalid formats
        self.assertFalse(self.registration.is_valid_email("userexample.com"))   # Missing @
        self.assertFalse(self.registration.is_valid_email("user@com"))          # No dot after @
        self.assertFalse(self.registration.is_valid_email("user@@example.com")) # Double @
        self.assertFalse(self.registration.is_valid_email("user@example"))      # Missing TLD
        self.assertFalse(self.registration.is_valid_email(""))
        self.assertFalse(self.registration.is_valid_email("@example.com"))
        self.assertFalse(self.registration.is_valid_email("user@.com"))

if __name__ == "__main__":
    unittest.main()