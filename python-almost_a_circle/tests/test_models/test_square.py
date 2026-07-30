#!/usr/bin/python3
"""Unittest for Square class"""
import unittest
import os
import json
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class"""

    def test_sq_1(self):
        """Test Square(1)"""
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_sq_1_2(self):
        """Test Square(1, 2)"""
        s = Square(1, 2)
        self.assertEqual(s.x, 2)

    def test_sq_1_2_3(self):
        """Test Square(1, 2, 3)"""
        s = Square(1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_sq_str_size(self):
        """Test Square string size raises TypeError"""
        with self.assertRaises(TypeError):
            Square("1")

    def test_sq_str_x(self):
        """Test Square string x raises TypeError"""
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_sq_str_y(self):
        """Test Square string y raises TypeError"""
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_sq_with_id(self):
        """Test Square with id"""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

    def test_sq_neg_size(self):
        """Test Square negative size raises ValueError"""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_sq_neg_x(self):
        """Test Square negative x raises ValueError"""
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_sq_neg_y(self):
        """Test Square negative y raises ValueError"""
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_sq_zero(self):
        """Test Square zero raises ValueError"""
        with self.assertRaises(ValueError):
            Square(0)

    def test_sq_str(self):
        """Test __str__() for Square"""
        s = Square(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 1")

    def test_sq_to_dict(self):
        """Test to_dictionary() in Square"""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.to_dictionary(),
                         {'id': 4, 'size': 1, 'x': 2, 'y': 3})

    def test_sq_update(self):
        """Test update() in Square"""
        s = Square(1)
        s.update()
        self.assertEqual(s.size, 1)

    def test_sq_update_89(self):
        """Test update(89) in Square"""
        s = Square(1)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_sq_update_89_1(self):
        """Test update(89, 1) in Square"""
        s = Square(1)
        s.update(89, 1)
        self.assertEqual(s.size, 1)

    def test_sq_update_89_1_2(self):
        """Test update(89, 1, 2) in Square"""
        s = Square(1)
        s.update(89, 1, 2)
        self.assertEqual(s.x, 2)

    def test_sq_update_89_1_2_3(self):
        """Test update(89, 1, 2, 3) in Square"""
        s = Square(1)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_sq_update_kw_id(self):
        """Test update kwargs id in Square"""
        s = Square(1)
        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_sq_update_kw_id_size(self):
        """Test update kwargs id size in Square"""
        s = Square(1)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)

    def test_sq_update_kw_id_size_x(self):
        """Test update kwargs id size x in Square"""
        s = Square(1)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_sq_update_kw_all(self):
        """Test update kwargs all in Square"""
        s = Square(1)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_sq_create_id(self):
        """Test Square create with id"""
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_sq_create_id_size(self):
        """Test Square create with id and size"""
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)

    def test_sq_create_id_size_x(self):
        """Test Square create with id size x"""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_sq_create_all(self):
        """Test Square create with all attributes"""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_sq_save_to_file_none(self):
        """Test Square save_to_file with None"""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")
        self.assertEqual(json.loads(content), [])

    def test_sq_save_to_file_empty(self):
        """Test Square save_to_file with empty list"""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")
        self.assertEqual(json.loads(content), [])

    def test_sq_save_to_file(self):
        """Test Square save_to_file with Square(1)"""
        s = Square(1)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            content = json.loads(f.read())
        self.assertEqual(len(content), 1)
        self.assertEqual(content[0]['size'], 1)

    def test_sq_load_from_file_no_file(self):
        """Test Square load_from_file when file doesnt exist"""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        result = Square.load_from_file()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    def test_sq_load_from_file(self):
        """Test Square load_from_file when file exists"""
        s = Square(1)
        Square.save_to_file([s])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 1)
        self.assertIsInstance(squares[0], Square)
        self.assertEqual(squares[0].size, 1)


if __name__ == '__main__':
    unittest.main()
