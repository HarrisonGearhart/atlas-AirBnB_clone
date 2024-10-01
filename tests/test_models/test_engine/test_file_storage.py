#!/usr/bin/python3
"""
file to hold unit test class
"""
import unittest
import models


class test(unittest.TestCase):
    def test__file_path(self):
        garb = models.base_model
        self.assertEqual(models.storage._FileStorage__file_path, "file.json")

if __name__ == "__main__":
    unittest.main()
