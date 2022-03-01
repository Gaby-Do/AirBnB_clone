#!/usr/bin/python3
"""
Defining class State

Public attributes:
    name: string
"""
from models.base_model import BaseModel


class State(BaseModel):
    name = ""

    def __str__(self):
        return f'[{__class__.__name__}] ({self.id}) {self.__dict__}'
