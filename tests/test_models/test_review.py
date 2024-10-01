#!/usr/bin/python3
"""
file to hold unit test class
"""
import unittest
from models.review import Review


class test(unittest.TestCase):
    """
    tests if the attributes of User are strings
    """
    def test_place_id_is_str(self):
        self.assertEqual(str, type(Review.place_id))
    def test_user_id_is_str(self):
        self.assertEqual(str, type(Review.user_id))
    def test_text_is_str(self):
        self.assertEqual(str, type(Review.text))


if __name__ == "__main__":
    unittest.main()
