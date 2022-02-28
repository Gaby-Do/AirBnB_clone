#!/usr/bin/python3
"""
class BaseModel that defines all common attributes/methods for other classes
"""
from datetime import datetime
from models import storage
from uuid import uuid4


class BaseModel():
    def __init__(self, *args, **kwargs):
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
        return f'[{__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        dictio = self.__dict__.copy()
        dictio["__class__"] = __class__.__name__
        dictio["created_at"] = self.created_at.isoformat()
        dictio["updated_at"] = self.created_at.isoformat()
        return dictio
