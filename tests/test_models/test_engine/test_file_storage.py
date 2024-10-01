#!/usr/bin/python3
"""
file to hold unit test class
"""
import unittest
import os
import models


class test(unittest.TestCase):
    def test___file_path(self):
        laugh = models.FileStorage
        self.assertTrue(laugh)

if __name__ == "__main__":
    unittest.main()
