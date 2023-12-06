#!/usr/bin/python3
"""This file contains a super class BaseModel
"""
import uuid
from datetime import datetime

class BaseModel:
	"""A BaseModel class
	"""
	def __init__(self):
		"""An init method for instances
		"""
		self.id = str(uuid.uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()
		
	def __str__(self):
		"""A string method

		Returns:
			str: For string output
		"""
		return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

	def save(self):    
		"""A save method to update time
		"""
		self.updated_at = datetime.now()        
		
		
	def to_dict(self):                   
		dictionary = self.__dict__.copy()
		dictionary["__class__"] = self.__class__.__name__
		dictionary["created_at"] = self.created_at.isoformat()
		dictionary["updated_at"] = self.updated_at.isoformat()

		return dictionary
