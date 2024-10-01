#!/usr/bin/python3
"""
file to hold unit test class
"""
import unittest
from models.state import State


class test(unittest.TestCase):
    """
    tests if the attributes of User are strings
    """
    def test_name_is_str(self):
        self.assertEqual(str, type(State.name))


if __name__ == "__main__":
    unittest.main()
