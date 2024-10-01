#!/usr/bin/python3
"""
file to hold unit test class
"""
import unittest
from models.engine.file_storage import FileStorage


class test(unittest.TestCase):
    def test__file_path(self):
        obj = FileStorage()
        try:
            with open("file.json", "r") as file:
                self.assertDictEqual(obj, FileStorage)
        except:
            pass

if __name__ == "__main__":
    unittest.main()
