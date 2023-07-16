#!/usr/bin/python6
# Author: MikiasHailu
# Project: Circle
""" new circle """
import sys
import io
import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle_instantiation(unittest.TestCase):
    """ This is the test rectangle class """

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(40, 4), Base)

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(4)

    def test_three_args(self):
        r4 = Rectangle(8, 8, 4)
        r4 = Rectangle(8, 8, 8)
        self.assertEqual(r4.id, r4.id - 4)

    def test_two_args(self):
        r4 = Rectangle(40, 8)
        r4 = Rectangle(8, 40)
        self.assertEqual(r4.id, r4.id - 4)

    def test_four_args(self):
        r4 = Rectangle(4, 8, 6, 8)
        r4 = Rectangle(8, 6, 8, 4)
        self.assertEqual(r4.id, r4.id - 4)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(4, 8, 6, 8, 40, 44)

    def test_five_args(self):
        self.assertEqual(7, Rectangle(40, 8, 0, 0, 48).id)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(40, 40, 0, 0, 4).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(40, 40, 0, 0, 4).__height)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(40, 40, 0, 0, 4).__y)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(40, 40, 0, 0, 4).__x)

    def test_height_getter(self):
        r = Rectangle(40, 48, 48, 40, 4)
        self.assertEqual(7, r.height)

    def test_width_setter(self):
        r = Rectangle(40, 48, 48, 40, 4)
        r.width = 40
        self.assertEqual(40, r.width)

   def test_width_getter(self):
       r = Rectangle(40, 48, 48, 40, 4)
        self.assertEqual(40, r.width)

    def test_height_setter(self):
        r = Rectangle(40, 48, 48, 40, 4)
        r.height = 40
        self.assertEqual(40, r.height)

    def test_x_setter(self):
        r = Rectangle(40, 48, 48, 40, 4)
        r.x = 40
        self.assertEqual(40, r.x)

    def test_x_getter(self):
        r = Rectangle(40, 48, 48, 40, 4)
        self.assertEqual(48, r.x)

    def test_y_setter(self):
        r = Rectangle(40, 48, 48, 40, 4)
        r.y = 40
        self.assertEqual(40, r.y)

    def test_y_getter(self):
        r = Rectangle(40, 48, 48, 40, 4)
        self.assertEqual(40, r.y)

class TestRectangle_width(unittest.TestCase):
    """ This is the test rectangle """

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 4)

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 4)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(10), 4)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(10.10, 4)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 4, "b": 4}, 4)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 4)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([4, 4, 6], 4)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({4, 4, 6}, 4)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((4, 4, 6), 4)

    def test_frozenset_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({4, 4, 6, 4}), 4)

    def test_range_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(10), 4)

    def test_bytes_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Python', 4)

    def test_bytearray_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'abcdefg'), 4)

    def test_memoryview_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'abcedfg'), 4)

    def test_inf_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 4)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-4, 4)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 4)

    def test_nan_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 4)

class TestRectangle_height(unittest.TestCase):
    """ This class testRectangle class """

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "invalid")

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, None)

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, 10.10)

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, complex(10))

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, {"a": 4, "b": 4})

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, [4, 4, 6])

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, {4, 4, 6})

    def test_frozenset_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, frozenset({4, 4, 6, 4}))

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, (4, 4, 6))

    def test_bytes_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, b'Python')

    def test_range_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, range(10))

    def test_bytearray_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, bytearray(b'abcdefg'))

    def test_memoryview_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, memoryview(b'abcedfg'))

    def test_inf_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, float('inf'))

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(4, -4)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(4, 0)

    def test_nan_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, float('nan'))

class TestRectangle_x(unittest.TestCase):
    """ this is the test rectangle class """

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 4, float('nan'), 4)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 4, "invalid", 4)

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 4, None)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 4, complex(10))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 4, {"a": 4, "b": 4}, 4)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 4, [4, 4, 6], 4)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 4, True, 4)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 4, {4, 4, 6}, 4)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 4, (4, 4, 6), 4)

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 4, frozenset({4, 4, 6, 4}))

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 4, b'Python')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 4, bytearray(b'abcdefg'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 4, memoryview(b'abcedfg'))

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 4, float('inf'), 4)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 6, -4, 0)


class TestRectangle_y(unittest.TestCase):
    """ This is test rectangle class """

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 4, 6, 10.10)

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 4, 6, None)

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 4, 4, (4, 4, 6))

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 4, 6, complex(10))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 4, 4, {"a": 4, "b": 4})

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 4, 4, "invalid")

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 4, 4, [4, 4, 6])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 4, 4, {4, 4, 6})

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 4, 6, frozenset({4, 4, 6, 4}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 4, 6, range(10))

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 4, 6, bytearray(b'abcdefg'))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 4, 6, b'Python')

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 4, 6, memoryview(b'abcedfg'))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 4, 4, float('inf'))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(6, 10, 0, -4)

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 4, 4, float('nan'))


class TestRectangle_order_of_initialization(unittest.TestCase):
    """ This is the rectangle order of initialization class """

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 4, 6, "invalid y")

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 4, "invalid x", "invalid y")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 4, "invalid x")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "invalid height", "invalid x")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "invalid height", 4, "invalid y")

class TestRectangle_area(unittest.TestCase):
    """Unittests for testing the area method of the Rectangle class."""

    def test_area_small(self):
        r = Rectangle(40, 4, 0, 0, 0)
        self.assertEqual(40, r.area())

    def test_area_large(self):
        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 4)
        self.assertEqual(999999999999998999000000000000004, r.area())

    def test_area_changed_attributes(self):
        r = Rectangle(4, 40, 4, 4, 4)
        r.width = 7
        r.height = 48
        self.assertEqual(98, r.area())

    def test_area_one_arg(self):
        r = Rectangle(4, 40, 4, 4, 4)
        with self.assertRaises(TypeError):
            r.area(4)


class TestRectangle_stdout(unittest.TestCase):
    """ This is the test rectangle std class """

    @staticmethod
    def capture_stdout(rect, method):
        """ This fucntion will take and return printed txt """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_width_height_x_y(self):
        r = Rectangle(4, 8, 4, 8)
        correct = "[Rectangle] ({}) 4/8 - 4/8".format(r.id)
        self.assertEqual(correct, str(r))

    def test_str_method_print_width_height(self):
        r = Rectangle(8, 6)
        capture = TestRectangle_stdout.capture_stdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 8/6\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_width_height_x(self):
        r = Rectangle(10, 10, 4)
        correct = "[Rectangle] ({}) 4/0 - 10/10".format(r.id)
        self.assertEqual(correct, r.__str__())

    def test_str_method_width_height_x_y_id(self):
        r = Rectangle(46, 44, 4, 8, 7)
        self.assertEqual("[Rectangle] (7) 4/8 - 46/44", str(r))

    def test_str_method_changed_attributes(self):
        r = Rectangle(7, 7, 0, 0, [8])
        r.width = 410
        r.height = 4
        r.x = 8
        r.y = 40
        self.assertEqual("[Rectangle] ([8]) 8/40 - 410/4", str(r))

    def test_str_method_one_arg(self):
        r = Rectangle(4, 4, 6, 8, 10)
        with self.assertRaises(TypeError):
            r.__str__(4)

    def test_display_width_height(self):
        r = Rectangle(4, 6, 0, 0, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_one_arg(self):
        r = Rectangle(10, 4, 4, 8, 7)
        with self.assertRaises(TypeError):
            r.display(4)

    def test_display_width_height_y(self):
        r = Rectangle(8, 10, 0, 4, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_width_height_x_y(self):
        r = Rectangle(4, 8, 6, 4, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_width_height_x(self):
        r = Rectangle(6, 4, 4, 0, 4)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

class TestRectangle_update_args(unittest.TestCase):
    """ This is the text rectangle update class """

    def test_update_args_zero(self):
        r = Rectangle(40, 40, 40, 40, 40)
        r.update()
        self.assertEqual("[Rectangle] (40) 40/40 - 40/40", str(r))

    def test_update_args_two(self):
        r = Rectangle(40, 40, 40, 40, 40)
        r.update(89, 4)
        self.assertEqual("[Rectangle] (89) 40/40 - 4/40", str(r))

    def test_update_args_one(self):
        r = Rectangle(40, 40, 40, 40, 40)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 40/40 - 40/40", str(r))

    def test_update_args_three(self):
        r = Rectangle(40, 40, 40, 40, 40)
        r.update(89, 4, 6)
        self.assertEqual("[Rectangle] (89) 40/40 - 4/6", str(r))

    def test_update_args_five(self):
        r = Rectangle(40, 40, 40, 40, 40)
        r.update(89, 4, 6, 8, 10)
        self.assertEqual("[Rectangle] (89) 8/10 - 4/6", str(r))

    def test_update_args_four(self):
        r = Rectangle(40, 40, 40, 40, 40)
        r.update(89, 4, 6, 8)
        self.assertEqual("[Rectangle] (89) 8/40 - 4/6", str(r))

    def test_update_args_more_than_five(self):
        r = Rectangle(40, 40, 40, 40, 40)
        r.update(89, 4, 6, 8, 10, 6)
        self.assertEqual("[Rectangle] (89) 8/10 - 4/6", str(r))

    def test_update_args_None_id(self):
        r = Rectangle(40, 40, 40, 40, 40)
        r.update(None)
        correct = "[Rectangle] ({}) 40/40 - 40/40".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_None_id_and_more(self):
        r = Rectangle(40, 40, 40, 40, 40)
        r.update(None, 8, 10, 4)
        correct = "[Rectangle] ({}) 4/40 - 8/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_twice(self):
        r = Rectangle(40, 40, 40, 40, 40)
        r.update(89, 4, 6, 8, 10, 6)
        r.update(6, 10, 8, 6, 4, 89)
        self.assertEqual("[Rectangle] (6) 6/4 - 10/8", str(r))

    def test_update_args_invalid_width_type(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")

    def test_update_args_width_negative(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, -10)

    def test_update_args_width_zero(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)

    def test_update_args_invalid_height_type(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 4, "invalid")

    def test_update_args_height_zero(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 4, 0)

    def test_update_args_height_negative(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 4, -10)

    def test_update_args_invalid_x_type(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 4, 6, "invalid")

    def test_update_args_x_negative(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 4, 4, -6)

    def test_update_args_invalid_y(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 4, 6, 8, "invalid")

    def test_update_args_y_negative(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 4, 4, 6, -6)

    def test_update_args_width_before_height(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", "invalid")

    def test_update_args_x_before_y(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 4, 4, "invalid", "invalid")

    def test_update_args_width_before_x(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 4, "invalid")

    def test_update_args_width_before_y(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 4, 4, "invalid")

    def test_update_args_height_before_x(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 4, "invalid", "invalid")

    def test_update_args_height_before_y(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 4, "invalid", 4, "invalid")

class TestRectangle_update_kwargs(unittest.TestCase):
    """ This is the testRectangle update class """

    def test_update_kwargs_x_negative(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-10)

    def test_update_kwargs_None_id_and_more(self):
        r = Rectangle(40, 40, 40, 40, 40)
        r.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 40/9 - 40/7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_four(self):
        r = Rectangle(40, 40, 40, 40, 40)
        r.update(id=89, x=4, height=4, y=6, width=8)
        self.assertEqual("[Rectangle] (89) 4/6 - 8/4", str(r))

    def test_update_kwargs_five(self):
        r = Rectangle(40, 40, 40, 40, 40)
        r.update(y=10, x=8, id=99, width=4, height=4)
        self.assertEqual("[Rectangle] (99) 8/10 - 4/4", str(r))

    def test_update_kwargs_one(self):
        r = Rectangle(40, 40, 40, 40, 40)
        r.update(id=4)
        self.assertEqual("[Rectangle] (4) 40/40 - 40/40", str(r))

    def test_update_kwargs_three(self):
        r = Rectangle(40, 40, 40, 40, 40)
        r.update(width=4, height=6, id=89)
        self.assertEqual("[Rectangle] (89) 40/40 - 4/6", str(r))

    def test_update_kwargs_two(self):
        r = Rectangle(40, 40, 40, 40, 40)
        r.update(width=4, id=4)
        self.assertEqual("[Rectangle] (4) 40/40 - 4/40", str(r))

    def test_update_kwargs_None_id(self):
        r = Rectangle(40, 40, 40, 40, 40)
        r.update(id=None)
        correct = "[Rectangle] ({}) 40/40 - 40/40".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        r = Rectangle(40, 40, 40, 40, 40)
        r.update(id=89, x=4, height=4)
        r.update(y=6, height=410, width=4)
        self.assertEqual("[Rectangle] (89) 4/6 - 4/410", str(r))

    def test_update_kwargs_invalid_width_type(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_width_negative(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-10)

    def test_update_kwargs_invalid_height_type(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_height_negative(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-10)

    def test_update_kwargs_inavlid_x_type(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_y_negative(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-10)

    def test_update_kwargs_some_wrong_keys(self):
        r = Rectangle(40, 40, 40, 40, 40)
        r.update(height=10, id=89, a=4, b=108, x=49, y=7)
        self.assertEqual("[Rectangle] (89) 49/7 - 40/10", str(r))

    def test_update_kwargs_invalid_y_type(self):
        r = Rectangle(40, 40, 40, 40, 40)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def test_update_args_and_kwargs(self):
        r = Rectangle(40, 40, 40, 40, 40)
        r.update(89, 4, height=8, y=6)
        self.assertEqual("[Rectangle] (89) 40/40 - 4/40", str(r))

    def test_update_kwargs_wrong_keys(self):
        r = Rectangle(40, 40, 40, 40, 40)
        r.update(a=10, b=40)
        self.assertEqual("[Rectangle] (40) 40/40 - 40/40", str(r))

class TestRectangle_to_dictionary(unittest.TestCase):
    """ This is the test rectangle to dictionary class """

    def test_to_dictionary_no_object_changes(self):
        r4 = Rectangle(40, 4, 4, 9, 10)
        r4 = Rectangle(10, 9, 4, 4, 40)
        r4.update(**r4.to_dictionary())
        self.assertNotEqual(r4, r4)

    def test_to_dictionary_output(self):
        r = Rectangle(40, 4, 4, 9, 10)
        correct = {'x': 4, 'y': 9, 'id': 10, 'height': 4, 'width': 40}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_arg(self):
        r = Rectangle(40, 4, 8, 4, 4)
        with self.assertRaises(TypeError):
            r.to_dictionary(4)

if __name__ == "__main__":
    unittest.main()
