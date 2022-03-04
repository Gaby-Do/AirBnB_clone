#!/usr/bin/python3
"""
Serializes instances to a JSON file and deserializes JSON file to instances
"""
import json


class FileStorage():
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    - Private class attributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - stores all objects by <class name>.id
    - Public instance methods:
        all(self)
        new(self, obj)
        save(self)
        reload(self)
    """
    def __init__(self):
        """
        Initializes class FileStorage

        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        aux_dic = {}
        with open(self.__file_path, 'w+', encoding='utf8') as my_j_file:
            for key, value in self.__objects.items():
                aux_dic[key] = value.to_dict()
            json.dump(aux_dic, my_j_file)

    def reload(self):
        """
        deserializes the JSON file to __objects, if file exists
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        try:
            with open(self.__file_path, 'r', encoding='utf8') as my_j_file:
                new_dic = json.load(my_j_file)
                for key, value in new_dic.items():
                    key_args = str(key).split('.')
                    self.__objects[key] = eval(key_args[0])(**value)
        except Exception:
            return
