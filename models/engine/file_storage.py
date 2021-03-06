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
    __file_path = "file.json"
    __objects = {}

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
        try:
            with open(self.__file_path, 'w+', encoding='utf8') as my_j_file:
                for key, value in self.__objects.items():
                    aux_dic[key] = value.to_dict()
                json.dump(aux_dic, my_j_file)
        except Exception:
            return

    def reload(self):
        """
        deserializes the JSON file to __objects, if file exists
        """
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        class_dict = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
                      "Place": Place, "Review": Review,
                      "State": State, "User": User}
        try:
            with open(self.__file_path, 'r', encoding='utf8') as my_j_file:
                new_dic = json.load(my_j_file)
                for key, value in new_dic.items():
                    key_args = str(key).split('.')
                    if key_args[0] in class_dict.keys():
                        self.__objects[key] = class_dict[key_args[0]](**value)
        except Exception:
            return
