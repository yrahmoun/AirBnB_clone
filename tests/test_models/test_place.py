#!/usr/bin/python3
"""Unit test for the Place class in the models module
"""
import unittest
import pep8
from models.place import Place
from models.base_model import BaseModel


class TestPlaceClass(unittest.TestCase):
    """TestPlaceClass test suite for the Place class."""

    maxDiff = None

    def setUp(self):
        """Set up before each test case."""
        Place.city_id = ""
        Place.user_id = ""
        Place.name = ""
        Place.description = ""
        Place.number_rooms = 0
        Place.number_bathrooms = 0
        Place.max_guest = 0
        Place.price_by_night = 0
        Place.latitude = 0.0
        Place.longitude = 0.0
        Place.amenity_ids = []

    def test_module_doc(self):
        """Check for module-level documentation."""
        self.assertTrue(len(place.__doc__) > 0)

    def test_class_doc(self):
        """Check for class-level documentation."""
        self.assertTrue(len(Place.__doc__) > 0)

    def test_method_docs(self):
        """Check for method documentation."""
        for method_name in dir(Place):
            self.assertTrue(len(getattr(Place, method_name).__doc__) > 0)

    def test_pep8(self):
        """Test Place and test_place for pep8 conformance."""
        style = pep8.StyleGuide(quiet=True)
        files = ["models/place.py", "tests/test_models/test_place.py"]
        result = style.check_files(files)
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warning)."
        )

    def test_is_instance(self):
        """Test if an instance of Place is also an instance of BaseModel."""
        my_place = Place()
        self.assertIsInstance(my_place, BaseModel)

    def test_field_types(self):
        """Test the field attributes of the Place class."""
        self.assertIsInstance(Place.city_id, str)
        self.assertIsInstance(Place.user_id, str)
        self.assertIsInstance(Place.name, str)
        self.assertIsInstance(Place.description, str)
        self.assertIsInstance(Place.number_rooms, int)
        self.assertIsInstance(Place.number_bathrooms, int)
        self.assertIsInstance(Place.max_guest, int)
        self.assertIsInstance(Place.price_by_night, int)
        self.assertIsInstance(Place.latitude, float)
        self.assertIsInstance(Place.longitude, float)
        self.assertIsInstance(Place.amenity_ids, list)


if __name__ == "__main__":
    unittest.main()
