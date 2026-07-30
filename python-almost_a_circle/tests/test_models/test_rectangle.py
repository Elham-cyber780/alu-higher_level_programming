#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
import os
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle


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

    def test_area(self):
        """Test area()"""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_str(self):
        """Test __str__() for Rectangle"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_display_no_x_y(self):
        """Test display() without x and y"""
        r = Rectangle(2, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "##\n##\n")

    def test_display_no_y(self):
        """Test display() without y"""
        r = Rectangle(2, 2, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), " ##\n ##\n")

    def test_display(self):
        """Test display()"""
        r = Rectangle(2, 2, 1, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "\n ##\n ##\n")

    def test_to_dictionary(self):
        """Test to_dictionary() in Rectangle"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.to_dictionary(),
                         {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4})

    def test_update(self):
        """Test update() in Rectangle"""
        r = Rectangle(1, 2)
        r.update()
        self.assertEqual(r.width, 1)

    def test_update_89(self):
        """Test update(89) in Rectangle"""
        r = Rectangle(1, 2)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_89_1(self):
        """Test update(89, 1) in Rectangle"""
        r = Rectangle(1, 2)
        r.update(89, 1)
        self.assertEqual(r.width, 1)

    def test_update_89_1_2(self):
        """Test update(89, 1, 2) in Rectangle"""
        r = Rectangle(1, 2)
        r.update(89, 1, 2)
        self.assertEqual(r.height, 2)

    def test_update_89_1_2_3(self):
        """Test update(89, 1, 2, 3) in Rectangle"""
        r = Rectangle(1, 2)
        r.update(89, 1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_update_89_1_2_3_4(self):
        """Test update(89, 1, 2, 3, 4) in Rectangle"""
        r = Rectangle(1, 2)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_update_kw_id(self):
        """Test update kwargs id in Rectangle"""
        r = Rectangle(1, 2)
        r.update(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_update_kw_id_width(self):
        """Test update kwargs id width in Rectangle"""
        r = Rectangle(1, 2)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

    def test_update_kw_id_width_height(self):
        """Test update kwargs id width height in Rectangle"""
        r = Rectangle(1, 2)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

    def test_update_kw_id_width_height_x(self):
        """Test update kwargs id width height x in Rectangle"""
        r = Rectangle(1, 2)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

    def test_update_kw_all(self):
        """Test update kwargs all in Rectangle"""
        r = Rectangle(1, 2)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_create_id(self):
        """Test Rectangle create with id"""
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_create_id_width(self):
        """Test Rectangle create with id and width"""
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

    def test_create_id_width_height(self):
        """Test Rectangle create with id width height"""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

    def test_create_id_width_height_x(self):
        """Test Rectangle create with id width height x"""
        r = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

    def test_create_all(self):
        """Test Rectangle create with all attributes"""
        r = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_save_to_file_none(self):
        """Test Rectangle save_to_file with None"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Test Rectangle save_to_file with empty list"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file(self):
        """Test Rectangle save_to_file with list"""
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as f:
            self.assertIn("width", f.read())

    def test_load_from_file_no_file(self):
        """Test Rectangle load_from_file when file doesnt exist"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file(self):
        """Test Rectangle load_from_file when file exists"""
        Rectangle.save_to_file([Rectangle(1, 2)])
        rects = Rectangle.load_from_file()
        self.assertIsInstance(rects[0], Rectangle)


if __name__ == '__main__':
    unittest.main()
