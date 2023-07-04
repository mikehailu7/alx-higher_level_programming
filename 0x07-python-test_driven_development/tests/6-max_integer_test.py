#!/usr/bin/python3
# Author: MikiasHailu
# Fun: maximum_integer

""" This module will Unittest for max_integer """

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """This class will unittest maximum integer. """
    def test_function_docstring(self):
        """This function will Tests for funstion docstring """
        g = max_integer.__doc__
        self.assertTrue(len(g) > 1)

    def test_module_docstring(self):
        """This funciton will Tests for module docsting"""
        z = __import__('6-max_integer').__doc__
        self.assertTrue(len(z) > 1)

    def test_empty_list(self):
        """This function will Tests for empty list """
        t = []
        self.assertIsNone(max_integer(t))

    def test_one_element(self):
        """ This funciton will Tests for one number only one number"""
        o = [1]
        self.assertEqual(max_integer(o), 1)

    def test_no_args(self):
        """ This function will tests for if there is no arg passed by other fun"""
        self.assertIsNone(max_integer())

    def test_positive_end(self):
        """ This function will Tests for the highest number"""
        t = [45, 55, 5, 20, 24, 80]
        self.assertEqual(max_integer(t), 80)
    def test_positive_beginning(self):
        """Tests for all positive with max at beginning"""
        k = [360, 100, 89, 34, 54, 50]
        self.assertEqual(max_integer(k), 360)

    def test_positive_middle(self):
        """Tests for all positive with max in middle"""
        z = [12, 100, 85, 500, 14, 50]
        self.assertEqual(max_integer(z), 500)

    def test_one_negative(self):
        """Tests for list with one negative number"""
        on = [200, 10, 8, -36, 14, 50]
        self.assertEqual(max_integer(on), 200)

    def test_all_negative(self):
        """Tests for list with all negative numbers"""
        n = [-6, -50, -75, -1, -100]
        self.assertEqual(max_integer(n), -1)

    def test_non_int_arg(self):
        """Tests for a non-int type in list"""
        string = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(string)
            
    def test_none(self):
        """Tests for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == "__main__":
    unittest.main()
