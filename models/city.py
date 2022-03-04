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
