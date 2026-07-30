#!/usr/bin/python3
"""Unittest for Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def test_id_auto(self):
        """Test auto id assignment"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_manual(self):
        """Test manual id assignment"""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_id_none(self):
        """Test None id assignment"""
        b = Base(None)
        self.assertIsNotNone(b.id)

    def test_id_string(self):
        """Test string id assignment"""
        b = Base("hello")
        self.assertEqual(b.id, "hello")

    def test_id_float(self):
        """Test float id assignment"""
        b = Base(1.5)
        self.assertEqual(b.id, 1.5)


if __name__ == '__main__':
    unittest.main()
