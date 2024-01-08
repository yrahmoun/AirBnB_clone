#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class TestBaseModelInit(unittest.TestCase):
    def test_init_with_kwargs(self):
        kwargs = {
            "created_at": "2022-01-01T12:34:56.789",
            "updated_at": "2022-01-02T15:45:30.123",
            "custom_attribute": "some_value",
        }

        instance = BaseModel(**kwargs)

        self.assertEqual(instance.created_at.isoformat(), "2022-01-01T12:34:56.789000")
        self.assertEqual(instance.updated_at.isoformat(), "2022-01-02T15:45:30.123000")

        self.assertEqual(instance.__dict__["custom_attribute"], "some_value")

    def test_init_without_kwargs(self):
        instance = BaseModel()

        self.assertIsNotNone(instance.id)
        self.assertIsNotNone(instance.created_at)
        self.assertIsNotNone(instance.updated_at)


if __name__ == "__main__":
    unittest.main()
