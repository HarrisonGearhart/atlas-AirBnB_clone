#!/usr/bin/python3
"""
file to hold unit test class
"""
import unittest
from models.user import User


class test(unittest.TestCase):
    """
    tests if the attributes of User are strings
    """
    def test_email_is_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_str(self):
        self.assertEqual(str, type(User.last_name))

if __name__ == "__main__":
    unittest.main()
