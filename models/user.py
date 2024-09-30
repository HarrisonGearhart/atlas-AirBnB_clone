#!/usr/bin/python3
"""User Class that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
	"""A user class that inherits from BaseModel
	Attributes - email, password, first_name, last_name (All empty strings)
	"""
	email = ""
	password = ""
	first_name = ""
	last_name = ""
