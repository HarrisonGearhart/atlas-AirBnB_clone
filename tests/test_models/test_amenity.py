#!/usr/bin/python3
"""
file to hold unit test class
"""
import unittest
from models.amenity import Amenity


class test(unittest.TestCase):
    def test_name_is_str(self):
        self.assertEqual(str, type(Amenity.name))


if __name__ == "__main__":
    unittest.main()
