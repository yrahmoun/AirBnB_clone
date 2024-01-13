#!/usr/bin/python3
""" unittests for models/base_model.py """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import os
import json


class TestBaseModel(unittest.TestCase):
    """ unittests for BaseModel"""

    def setUp(self):
        """Creates an instance of BaseModel for testing."""
        self.base_model = BaseModel()

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_init(self):
        """Test the initialization of a BaseModel instance."""
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_init_with_kwargs(self):
        """Test initialization of BaseModel with keyword arguments."""
        data = {
            'id': '123',
            'created_at': '2022-01-01T00:00:00.000000',
            'updated_at': '2022-01-02T00:00:00.000000',
            'custom_attr': 'value'
        }
        base_model = BaseModel(**data)
        self.assertEqual(base_model.id, '123')
        self.assertEqual(base_model.custom_attr, 'value')
        self.assertEqual(base_model.created_at, datetime(2022, 1, 1))
        self.assertEqual(base_model.updated_at, datetime(2022, 1, 2))

    def test_str(self):
        """Test the string representation of a BaseModel instance."""
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id,
                                                    self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_save(self):
        """Test saving a BaseModel instance and checking the file content."""
        self.base_model.save()
        with open("file.json", "r") as f:
            data = json.load(f)
            self.assertIn("BaseModel.{}".format(self.base_model.id), data)

    def test_to_dict(self):
        """Test converting a BaseModel instance to a dictionary."""
        expected_dict = {
            'id': self.base_model.id,
            '__class__': 'BaseModel',
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat()
        }
        self.assertEqual(self.base_model.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
