#!/usr/bin/python3
"""
Defining class Review

Attributes:
    place_id: string
    user_id: string
    text: string
"""
from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""

    def __str__(self):
        return f'[{__class__.__name__}] ({self.id}) {self.__dict__}'
