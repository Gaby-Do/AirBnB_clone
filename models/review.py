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
    """class Review, inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
