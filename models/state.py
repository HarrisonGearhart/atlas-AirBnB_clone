#!/usr/bin/python3
"""defines a state class that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
	"""
	class represtenting what state the rental property is located
	attributes-
	name (empty string)
	"""
	name = ""
