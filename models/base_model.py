#!/usr/bin/python3
""" Class Model Module"""
from uuid import uuid
from datetime import datetime

class BaseModel:
    """ Define all common attributes/methods for other classes """

    def __init__(self, id, created_at, updated_at):
        """ Init Base Model """
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
    
    def id(self):
        """ id Base Model """
        self.id = str(uuid.uuid4())

    def created_at(self):
        """ Assign with the current datetime when an instance is created
        """
        self.created_at = datetime.now()

    def updated_at(self):
        """ Assign with the current datetime when an instance is created and it will be updated every time you change your object
        """
        self.updated_at = datetime.now()

    def __str__(self):
        """ Print: [<class name>] (<self.id>) <self.__dict__> 
        """
        print("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """  Updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        
    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ of the instance
        """
        dict = self.___dict__.copy()
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        dict["__class__"] = self.__class__.__name__
        return dict