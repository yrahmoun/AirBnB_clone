#!/usr/bin/python3
"""Unit test for the Amenity class in the models module
"""
import unittest
import pep8
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage
import os


class TestAmenityClass(unittest.TestCase):
    """Test Amenity class for inheritance and attributes."""

    def tearDown(self):
        """Tear down after each test case."""
        storage._FileStorage__file_path = "file.json"
        try:
            os.remove("test.json")
        except FileNotFoundError:
            pass

    def setUp(self):
        """Set up before each test case."""
        with open("test.json", "w"):
            storage._FileStorage__file_path = "test.json"
            storage._FileStorage__objects = {}
        Amenity.name = ""

    def test_module_doc(self):
        """Check for module-level documentation."""
        self.assertTrue(len(amenity.__doc__) > 0)

    def test_class_doc(self):
        """Check for class-level documentation."""
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_method_docs(self):
        """Check for method documentation."""
        for method_name in dir(Amenity):
            self.assertTrue(len(getattr(Amenity, method_name).__doc__) > 0)

    def test_pep8(self):
        """Test Amenity and test_amenity for pep8 conformance."""
        style = pep8.StyleGuide(quiet=True)
        files = ["models/amenity.py", "tests/test_models/test_amenity.py"]
        result = style.check_files(files)
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warning)."
        )

    def test_is_instance(self):
        """Test if an instance of Amenity is also an instance of BaseModel."""
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity, BaseModel)

    def test_field_types(self):
        """Test the field attributes of the Amenity class."""
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity.name, str)


if __name__ == "__main__":
    unittest.main()
