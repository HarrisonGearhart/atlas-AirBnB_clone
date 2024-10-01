#!/usr/bin/python3
"""
file to hold unit test class
"""
import unittest
from models.engine.file_storage import FileStorage


class test(unittest.TestCase):
    def test__file_path(self):
        garb = FileStorage()
        self.assertEqual(self._FileStorage__file_path, "file.json")

if __name__ == "__main__":
    unittest.main()
