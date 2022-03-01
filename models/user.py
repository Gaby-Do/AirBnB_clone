#!/usr/bin/python3
"""
Defining class User

Public attributes:
    email: string
    password: string
    first_name: string
    last_name: string
"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User, inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __str__(self):
        """formats how __str__ will be printed"""
        return f'[{__class__.__name__}] ({self.id}) {self.__dict__}'
