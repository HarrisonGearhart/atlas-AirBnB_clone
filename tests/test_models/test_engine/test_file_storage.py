#!/usr/bin/python3
"""
file to hold unit test class
"""
import unittest
import os
import models


class test(unittest.TestCase):
    def test__file_path(self):
        brick = models.engine.file_storage.FileStorage()
        with open(brick._FileStorage__file_path, "r") as file:
            self.assertTrue(True)
        

if __name__ == "__main__":
    unittest.main()
