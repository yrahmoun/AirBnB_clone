#!/usr/bin/python3
"""Unit test for the State class in the models module
"""
import unittest
import pep8
from models.state import State
from models.base_model import BaseModel


class TestStateClass(unittest.TestCase):
    """Test suite for the State class."""

    maxDiff = None

    def setUp(self):
        """Set up before each test case."""
        State.name = ""

    def test_module_documentation(self):
        """Check for module-level documentation."""
        self.assertTrue(len(state.__doc__) > 0)

    def test_class_documentation(self):
        """Check for class-level documentation."""
        self.assertTrue(len(State.__doc__) > 0)

    def test_method_documentation(self):
        """Check for method documentation."""
        for method_name in dir(State):
            self.assertTrue(len(getattr(State, method_name).__doc__) > 0)

    def test_pep8_conformance(self):
        """Test State and test_state for pep8 conformance."""
        style = pep8.StyleGuide(quiet=True)
        files = ["models/state.py", "tests/test_models/test_state.py"]
        result = style.check_files(files)
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warning)."
        )

    def test_instance_of_base_model(self):
        """Test if an instance of State is also an instance of BaseModel."""
        my_state = State()
        self.assertIsInstance(my_state, BaseModel)

    def test_field_types(self):
        """Test the field attributes of the State class."""
        self.assertIsInstance(State.name, str)


if __name__ == "__main__":
    unittest.main()
