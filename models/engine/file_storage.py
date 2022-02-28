#!/usr/bin/python3
"""
serializes instances to a JSON file and deserializes JSON file to instances
"""
import json


class FileStorage():
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj.to_dict()

    def save(self):
        with open(self.__file_path, 'w+', encoding='utf8') as my_j_file:
            json.dump(self.__objects, my_j_file)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding='utf8') as my_j_file:
                self.__objects = json.load(my_j_file)
        except Exception:
            return
