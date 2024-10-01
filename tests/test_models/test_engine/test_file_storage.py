#!/usr/bin/python3
"""
file to hold unit test class
"""
import unittest
import os
import models


class test(unittest.TestCase):
    def test__file_path(self):
        a = models.engine.file_storage.FileStorage()
    try:
        with open(a._FileStorage__file_path, "r") as file:
            self.assertTrue(a._FileStorage__file_path)
    except:
        pass

if __name__ == "__main__":
    unittest.main()
