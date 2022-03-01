#!/usr/bin/python3
"""
Defining class BaseModel that defines all\n
common attributes/methods for other classes
"""
from datetime import datetime
from models import storage
from uuid import uuid4


class BaseModel():
    """
    Defining class BaseModel that defines all\n
    common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes class BaseModel
        
        Public attributes:
            id: string, asigned with uuid when an instance is created
            created_at: datetime - assigned with the current datetime\n
            when an instance is created
            updated_at: datetime - assigned with the current datetime\n
            when an instance is created and it will be updated\n
            every time the object is changed
        
        Arguments:
            *args: isnt't used
            **kwargs: dictionary that contains all arguments by key/value
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime
                            (value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        formats the way in which the string representation will be printed
        """
        return f'[{__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        dictio = self.__dict__.copy()
        dictio["__class__"] = self.__class__.__name__
        dictio["created_at"] = self.created_at.isoformat()
        dictio["updated_at"] = self.created_at.isoformat()

        return dictio
