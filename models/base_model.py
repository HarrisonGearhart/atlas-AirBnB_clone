#!/usr/bin/python3
"""
This is a file holding a base class that will be inherited by
many other classes
"""
import uuid


class BaseModel:
	def __init__(self, id, created_at, updated_at):
		self.id = str(uuid.uuid4())