#!/usr/bin/python3
"""
file to hold unit test class
"""
import unittest
from models.engine.file_storage import FileStorage


class test(unittest.TestCase):
    def test__file_path(self):
        obj = FileStorage()
        self.assertEqual(obj.__file_path, "file.json")
