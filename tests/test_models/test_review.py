#!/usr/bin/python3
"""Unit tests for the review module."""
import os
import unittest
from models.review import Review
from models import storage
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Reset FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_parameters(self):
        """Test method for class attributes"""

        review1 = Review()
        review3 = Review("hello", "wait", "in")
        key = f"{type(review1).__name__}.{review1.id}"
        self.assertIsInstance(review1.text, str)
        self.assertIsInstance(review1.user_id, str)
        self.assertIsInstance(review1.place_id, str)
        self.assertEqual(review3.text, "")

    def test_initialization(self):
        """Test method for public instances"""
        review1 = Review()
        review2 = Review(**review1.to_dict())
        self.assertIsInstance(review1.id, str)
        self.assertIsInstance(review1.created_at, datetime)
        self.assertIsInstance(review1.updated_at, datetime)
        self.assertEqual(review1.updated_at, review2.updated_at)

    def test_str_representation(self):
        """Test method for str representation"""
        review1 = Review()
        string = f"[{type(review1).__name__}] ({review1.id}) {review1.__dict__}"
        self.assertEqual(review1.__str__(), string)

    def test_save_method(self):
        """Test method for save"""
        review1 = Review()
        old_update = review1.updated_at
        review1.save()
        self.assertNotEqual(review1.updated_at, old_update)

    def test_to_dict_method(self):
        """Test method for dict"""
        review1 = Review()
        review2 = Review(**review1.to_dict())
        review_dict = review2.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['__class__'], type(review2).__name__)
        self.assertIn('created_at', review_dict.keys())
        self.assertIn('updated_at', review_dict.keys())
        self.assertNotEqual(review1, review2)


if __name__ == "__main__":
    unittest.main()
