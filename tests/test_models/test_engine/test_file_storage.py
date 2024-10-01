#!/usr/bin/python3
"""
file to hold unit test class
"""
import unittest
import models
import os


class test(unittest.TestCase):
    def test__file_path(self):
        my_file = models.storage._FileStorage__file_path
        path = os.getcwd() + "/" + my_file
        self.assertTrue(os.path.isfile(path))


if __name__ == "__main__":
    unittest.main()
