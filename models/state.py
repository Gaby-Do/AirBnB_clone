#!/usr/bin/python3
"""
Defining class State

Public attributes:
    name: string
"""
from models.base_model import BaseModel


class State(BaseModel):
    """class State, inherits from BaseModel"""
    name = ""

    def __str__(self):
        """format how __str__ will be printed"""
        return f'[{__class__.__name__}] ({self.id}) {self.__dict__}'
