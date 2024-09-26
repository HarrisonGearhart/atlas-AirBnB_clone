#!/usr/bin/python3
"""
file to hold unit test class
"""
import unittest
from models.base_model import BaseModel


class test(unittest.TestCase):
	"""
	tests if updated time is changed
	"""
	def test_save(self):
		a = BaseModel()
		save1 = a.updated_at
		a.save()
		save2 = a.updated_at
		self.assertNotEqual(save1, save2)

if __name__ == "__main__":
	unittest.main()
