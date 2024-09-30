#!/usr/bin/python3
"""defines a review class that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
	"""
	class represtenting the review the user gives of their experience
	attributes-
	place_id: string - empty string: it will be the Place.id
	user_id: string - empty string: it will be the User.id
	text: string - empty string
	"""
	place_id = ""
	user_id = ""
	text = ""
