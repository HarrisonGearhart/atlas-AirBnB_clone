#!/usr/bin/python3
"""
This is a file holding a base class that will be inherited by
many other classes
"""
import uuid
from datetime import datetime


class BaseModel:
	def __init__(self):
		self.id = str(uuid.uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()

	def __str__(self):
		return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

	def save(self):
		"""
		updates the updated_at attribute
		"""
		self.updated_at = datetime.now()

	def to_dict(self):
		"""
		This is a coversion of a instance to dictionary
		"""
		temp = {
			"id": self.id,
			"created_at": self.created_at.isoformat(),
			"updated_at": self.updated_at.isoformat(),
		}
		return temp
