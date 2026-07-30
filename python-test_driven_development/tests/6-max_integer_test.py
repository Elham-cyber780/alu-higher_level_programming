#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_max_at_end(self):
        """Test max at the end of list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test max at the beginning of list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test max in the middle of list"""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one_negative(self):
        """Test one negative number in list"""
        self.assertEqual(max_integer([1, -2, 3, 4]), 4)

    def test_only_negatives(self):
        """Test only negative numbers in list"""
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_one_element(self):
        """Test list with one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test empty list returns None"""
        self.assertIsNone(max_integer([]))

    def test_equal_elements(self):
        """Test list with equal elements"""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_floats(self):
        """Test list with floats"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)


if __name__ == '__main__':
    unittest.main()
