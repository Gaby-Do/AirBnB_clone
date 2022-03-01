#!/usr/bin/python3
"""
Defining class City

Public attributes:
    state_id: string
    name: string
"""
from models.base_model import BaseModel


class City(BaseModel):
    """class City, inherits from BaseModel"""
    state_id = ""
    name = ""

    def __str__(self):
        """formats how __str__ will be printed"""
        return f'[{__class__.__name__}] ({self.id}) {self.__dict__}'
