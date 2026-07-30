#!/usr/bin/python3
"""Unittest for Base Rectangle and Square classes"""
import unittest
import os
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_to_json_string_none(self):
        """Test to_json_string with None"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test to_json_string with empty list"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        """Test to_json_string with list"""
        result = Base.to_json_string([{'id': 12}])
        self.assertIn("12", result)

    def test_to_json_string_returns_string(self):
        """Test to_json_string returns a string"""
        self.assertIsInstance(Base.to_json_string([{'id': 12}]), str)

    def test_from_json_string_none(self):
        """Test from_json_string with None"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test from_json_string with empty string"""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_list(self):
        """Test from_json_string with list"""
        self.assertEqual(
            Base.from_json_string('[{"id": 89}]'), [{"id": 89}])

    def test_from_json_string_returns_list(self):
        """Test from_json_string returns a list"""
        self.assertIsInstance(
            Base.from_json_string('[{"id": 89}]'), list)


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def test_rect_1_2(self):
        """Test Rectangle(1, 2)"""
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)

    def test_rect_1_2_3(self):
        """Test Rectangle(1, 2, 3)"""
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_rect_1_2_3_4(self):
        """Test Rectangle(1, 2, 3, 4)"""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_rect_str_width(self):
        """Test Rectangle string width raises TypeError"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_rect_str_height(self):
        """Test Rectangle string height raises TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_rect_str_x(self):
        """Test Rectangle string x raises TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_rect_str_y(self):
        """Test Rectangle string y raises TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_rect_with_id(self):
        """Test Rectangle with id"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_rect_neg_width(self):
        """Test Rectangle negative width raises ValueError"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rect_neg_height(self):
        """Test Rectangle negative height raises ValueError"""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_rect_zero_width(self):
        """Test Rectangle zero width raises ValueError"""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rect_zero_height(self):
        """Test Rectangle zero height raises ValueError"""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rect_neg_x(self):
        """Test Rectangle negative x raises ValueError"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_rect_neg_y(self):
        """Test Rectangle negative y raises ValueError"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_rect_area(self):
        """Test area()"""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_rect_str(self):
        """Test __str__() for Rectangle"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_rect_display_no_x_y(self):
        """Test display() without x and y"""
        r = Rectangle(2, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "##\n##\n")

    def test_rect_display_no_y(self):
        """Test display() without y"""
        r = Rectangle(2, 2, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), " ##\n ##\n")

    def test_rect_display(self):
        """Test display()"""
        r = Rectangle(2, 2, 1, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "\n ##\n ##\n")

    def test_rect_to_dict(self):
        """Test to_dictionary() in Rectangle"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.to_dictionary(),
                         {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4})

    def test_rect_update(self):
        """Test update() in Rectangle"""
        r = Rectangle(1, 2)
        r.update()
        self.assertEqual(r.width, 1)

    def test_rect_update_89(self):
        """Test update(89) in Rectangle"""
        r = Rectangle(1, 2)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_rect_update_89_1(self):
        """Test update(89, 1) in Rectangle"""
        r = Rectangle(1, 2)
        r.update(89, 1)
        self.assertEqual(r.width, 1)

    def test_rect_update_89_1_2(self):
        """Test update(89, 1, 2) in Rectangle"""
        r = Rectangle(1, 2)
        r.update(89, 1, 2)
        self.assertEqual(r.height, 2)

    def test_rect_update_89_1_2_3(self):
        """Test update(89, 1, 2, 3) in Rectangle"""
        r = Rectangle(1, 2)
        r.update(89, 1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_rect_update_89_1_2_3_4(self):
        """Test update(89, 1, 2, 3, 4) in Rectangle"""
        r = Rectangle(1, 2)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_rect_update_kw_id(self):
        """Test update kwargs id in Rectangle"""
        r = Rectangle(1, 2)
        r.update(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_rect_update_kw_id_width(self):
        """Test update kwargs id width in Rectangle"""
        r = Rectangle(1, 2)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

    def test_rect_update_kw_id_width_height(self):
        """Test update kwargs id width height in Rectangle"""
        r = Rectangle(1, 2)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

    def test_rect_update_kw_id_width_height_x(self):
        """Test update kwargs id width height x in Rectangle"""
        r = Rectangle(1, 2)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

    def test_rect_update_kw_all(self):
        """Test update kwargs all in Rectangle"""
        r = Rectangle(1, 2)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_rect_create_id(self):
        """Test Rectangle create with id"""
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_rect_create_id_width(self):
        """Test Rectangle create with id and width"""
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

    def test_rect_create_id_width_height(self):
        """Test Rectangle create with id width height"""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

    def test_rect_create_id_width_height_x(self):
        """Test Rectangle create with id width height x"""
        r = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

    def test_rect_create_all(self):
        """Test Rectangle create with all attributes"""
        r = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_rect_save_to_file_none(self):
        """Test Rectangle save_to_file with None"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_rect_save_to_file_empty(self):
        """Test Rectangle save_to_file with empty list"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_rect_save_to_file(self):
        """Test Rectangle save_to_file with list"""
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as f:
            self.assertIn("width", f.read())

    def test_rect_load_from_file_no_file(self):
        """Test Rectangle load_from_file when file doesnt exist"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_rect_load_from_file(self):
        """Test Rectangle load_from_file when file exists"""
        Rectangle.save_to_file([Rectangle(1, 2)])
        rects = Rectangle.load_from_file()
        self.assertIsInstance(rects[0], Rectangle)


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
            self.assertEqual(f.read(), "[]")

    def test_sq_save_to_file_empty(self):
        """Test Square save_to_file with empty list"""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_sq_save_to_file(self):
        """Test Square save_to_file with list"""
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as f:
            self.assertIn("size", f.read())

    def test_sq_load_from_file_no_file(self):
        """Test Square load_from_file when file doesnt exist"""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_sq_load_from_file(self):
        """Test Square load_from_file when file exists"""
        Square.save_to_file([Square(1)])
        squares = Square.load_from_file()
        self.assertIsInstance(squares[0], Square)


if __name__ == '__main__':
    unittest.main()
