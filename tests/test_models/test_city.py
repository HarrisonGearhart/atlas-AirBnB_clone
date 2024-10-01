#!/usr/bin/python3
"""
file to hold unit test class
"""
import unittest
from models.city import City


class test(unittest.TestCase):
    def test_state_id_is_str(self):
        self.assertEqual(str, type(City.state_id))
    def test_name_is_str(self):
        self.assertEqual(str, type(City.name))

if __name__ == "__main__":
    unittest.main()
