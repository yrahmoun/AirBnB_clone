#!/usr/bin/python3
"""Unit test for the User class in the models module
"""
import unittest
import pep8
from models.user import User
from models.base_model import BaseModel


class TestUserClass(unittest.TestCase):
    """Test suite for the User class."""

    maxDiff = None

    def setUp(self):
        """Set up before each test case."""
        User.email = ""
        User.password = ""
        User.first_name = ""
        User.last_name = ""

    def test_module_documentation(self):
        """Check for module-level documentation."""
        self.assertTrue(len(user.__doc__) > 0)

    def test_class_documentation(self):
        """Check for class-level documentation."""
        self.assertTrue(len(User.__doc__) > 0)

    def test_method_documentation(self):
        """Check for method documentation."""
        for method_name in dir(User):
            self.assertTrue(len(getattr(User, method_name).__doc__) > 0)

    def test_pep8_conformance(self):
        """Test User and test_user for pep8 conformance."""
        style = pep8.StyleGuide(quiet=True)
        files = ["models/user.py", "tests/test_models/test_user.py"]
        result = style.check_files(files)
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warning)."
        )

    def test_instance_of_base_model(self):
        """Test if an instance of User is also an instance of BaseModel."""
        my_user = User()
        self.assertIsInstance(my_user, BaseModel)

    def test_field_types(self):
        """Test the field attributes of the User class."""
        self.assertIsInstance(User.email, str)
        self.assertIsInstance(User.password, str)
        self.assertIsInstance(User.first_name, str)
        self.assertIsInstance(User.last_name, str)


if __name__ == "__main__":
    unittest.main()
