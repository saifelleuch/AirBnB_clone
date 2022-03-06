#!/usr/bin/python3
""" Class Model Module"""
from asyncio.windows_events import NULL
from uuid import uuid
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ Define all common attributes/methods for other classes """
    def __init__(self, *args, **kwargs):
        """ Init Base Model """
        if kwargs is not NULL:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    new_value = datetime.strptime(value, time)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Print: [<class name>] (<self.id>) <self.__dict__> """
        print("[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """  Updates the public instance attribute \
            updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing \
            all keys/values of __dict__ of the instance
        """
        dict = self.___dict__.copy()
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        dict["__class__"] = self.__class__.__name__
        return dict
