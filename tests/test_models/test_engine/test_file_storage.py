#!/usr/bin/python3
"""
file to hold unit test class
"""
import unittest
import models


class test(unittest.TestCase):
    def test__file_path(self):
        try:
            with open(models.storage._FileStorage__file_path) as file:
                self.assertEqual(1, 1)
        except:
            self.asssertEqual(1, 2)
            pass


if __name__ == "__main__":
    unittest.main()
