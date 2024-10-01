#!/usr/bin/python3
"""
file to hold unit test class
"""
import unittest
import os
import models


class test(unittest.TestCase):
    def test__file_path(self):
        path = models.storage._FileStorage__file_path
        self.assertTrue(path, "OK")
        

if __name__ == "__main__":
    unittest.main()
