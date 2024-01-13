#!/usr/bin/python3
"""Unit test for the City class in the models module
"""
import unittest
import pep8
from models.city import City
from models.base_model import BaseModel


class TestCityClass(unittest.TestCase):
    """TestCityClass test suite for the City class."""

    maxDiff = None

    def setUp(self):
        """Set up before each test case."""
        City.name = ""
        City.state_id = ""

    def test_module_doc(self):
        """Check for module-level documentation."""
        self.assertTrue(len(city.__doc__) > 0)

    def test_class_doc(self):
        """Check for class-level documentation."""
        self.assertTrue(len(City.__doc__) > 0)

    def test_method_docs(self):
        """Check for method documentation."""
        for method_name in dir(City):
            self.assertTrue(len(getattr(City, method_name).__doc__) > 0)

    def test_pep8(self):
        """Test City and test_city for pep8 conformance."""
        style = pep8.StyleGuide(quiet=True)
        files = ["models/city.py", "tests/test_models/test_city.py"]
        result = style.check_files(files)
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warning)."
        )

    def test_is_instance(self):
        """Test if an instance of City is also an instance of BaseModel."""
        my_city = City()
        self.assertIsInstance(my_city, BaseModel)

    def test_field_types(self):
        """Test the field attributes of the City class."""
        self.assertIsInstance(City.name, str)
        self.assertIsInstance(City.state_id, str)


if __name__ == "__main__":
    unittest.main()
