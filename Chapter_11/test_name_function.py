#!../ENV/bin/python
# Testing functions
# import unittest
# import (function to test)
# Define a class that inherits the unittest.TestCase by
# class abc(unittest.TestCase)


import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """Test name_function"""
    # Create a function that starts with test
    # The interpreter automatically runs the function starting with test_

    def test_first_last_name(self):
        """Do names like Jake Herwitz work?"""
        # Create a variable for storing the results of the function
        formatted_name = get_formatted_name('jake', 'herwitz')
        # Run unittest.assert() method on the varaible and expected output
        # by using self.assertEqual(var, output)
        self.assertEqual(formatted_name, 'Jake Herwitz')
        # If the test was successful, OK will be output to the screen
        # Else the error report will be output

    # Adding new tests with function starting with test_
    def test_first_middle_last_name(self):
        """Do names with middle name work?"""
        formatted_name = get_formatted_name('jake', 'herwitz', 'blumenfeld')
        self.assertEqual(formatted_name, 'Jake Blumenfeld Herwitz')

unittest.main()
