import unittest
import User_Registration

def email_validation_stub(email):
    if email == "valid@test.com":
        return True
    return False


class TestEmailValidationWithStub(unittest.TestCase):

    def test_stubbed_email_validation(self):
        # Inject stub
        User_Registration.is_valid_email = email_validation_stub

        # Test behavior using stubbed responses
        self.assertTrue(User_Registration.is_valid_email("valid@test.com"))
        self.assertFalse(User_Registration.is_valid_email("wrong@example.com"))