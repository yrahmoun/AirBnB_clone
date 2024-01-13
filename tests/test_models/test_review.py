#!/usr/bin/python3
"""Unit test for the Review class in the models module
"""
import unittest
import pep8
from models.review import Review
from models.base_model import BaseModel


class TestReviewClass(unittest.TestCase):
    """TestReviewClass test suite for the Review class."""

    maxDiff = None

    def setUp(self):
        """Set up before each test case."""
        Review.place_id = ""
        Review.user_id = ""
        Review.text = ""

    def test_module_doc(self):
        """Check for module-level documentation."""
        self.assertTrue(len(review.__doc__) > 0)

    def test_class_doc(self):
        """Check for class-level documentation."""
        self.assertTrue(len(Review.__doc__) > 0)

    def test_method_docs(self):
        """Check for method documentation."""
        for method_name in dir(Review):
            self.assertTrue(len(getattr(Review, method_name).__doc__) > 0)

    def test_pep8(self):
        """Test Review and test_review for pep8 conformance."""
        style = pep8.StyleGuide(quiet=True)
        files = ["models/review.py", "tests/test_models/test_review.py"]
        result = style.check_files(files)
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warning)."
        )

    def test_is_instance(self):
        """Test if an instance of Review is also an instance of BaseModel."""
        my_review = Review()
        self.assertIsInstance(my_review, BaseModel)

    def test_field_types(self):
        """Test the field attributes of the Review class."""
        self.assertIsInstance(Review.place_id, str)
        self.assertIsInstance(Review.user_id, str)
        self.assertIsInstance(Review.text, str)


if __name__ == "__main__":
    unittest.main()
