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