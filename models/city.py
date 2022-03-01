#!/usr/bin/python3
"""
Defining class City

Public attributes:
    state_id: string
    name: string
"""
from models.base_model import BaseModel


class City(BaseModel):
    state_id = ""
    name = ""

    def __str__(self):
        return f'[{__class__.__name__}] ({self.id}) {self.__dict__}'
