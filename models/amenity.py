#!/usr/bin/python3
"""defines a amenity class that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
	"""
	class represtenting the aneninities associated with the property
	attributes-
	name (empty string)
	"""
	name = ""