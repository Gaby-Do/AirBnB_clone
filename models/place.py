#!/usr/bin/python3
"""
Defining class Place

Public attributes:
    city_id: string
    user_id: string
    name: string
    description: string
    number_rooms: integer - 0
    number_bathrooms: integer - 0
    max_guest: integer - 0
    price_by_night: integer - 0
    latitude: float
    longitude: float
    amenity_ids: list of string
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """class Place, inherits from BaseModel"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = int(0)
    number_bathrooms = int(0)
    max_guest = int(0)
    price_by_night = int(0)
    latitude = float(0.0)
    longitude = float(0.0)
    amenity_ids = []

    def __str__(self):
        """formats how __str__ will be printed"""
        return f'[{__class__.__name__}] ({self.id}) {self.__dict__}'
