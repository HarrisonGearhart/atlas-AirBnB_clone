#!/usr/bin/python3
"""
file to hold unit test class
"""
import unittest
import models
import os

import models.base_model


class test(unittest.TestCase):
    def test__file_path(self):
        test = models.base_model
        my_file = models.storage._FileStorage__file_path
        path = os.getcwd() + "/" + my_file
        self.assertTrue(os.path.isfile(path))


if __name__ == "__main__":
    unittest.main()
