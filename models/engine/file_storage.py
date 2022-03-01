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
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        aux_dic = {}
        with open(self.__file_path, 'w+', encoding='utf8') as my_j_file:
            for key, value in self.__objects.items():
                aux_dic[key] = value.to_dict()
            json.dump(aux_dic, my_j_file)


    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        try:
            with open(self.__file_path, 'r', encoding='utf8') as my_j_file:
                new_dic = json.load(my_j_file)
                for key, value in new_dic.items():
                    key_args = str(key).split('.')
                    self.__objects[key] = eval(key_args[0])(**value)
        except Exception:
            return
