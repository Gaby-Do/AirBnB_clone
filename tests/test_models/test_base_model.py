#!/usr/bin/python3
"""
Unittest for base_model
"""
from datetime import datetime
import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):

    def chech_docstring(self):
        """function to check docstring fo Basemodel"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_str(self):
        """testing str method"""
        model = BaseModel()
        model_str = '[{}] ({}) {}'.format(
                BaseModel.__name__, model.id, model.__dict__)
        self.assertEqual(model_str, str(model))

    def test_base_model(self):
        """testing basic stuff for a base model obj"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        # checking attribute types and class
        self.assertEqual(type(my_model), BaseModel)
        # id
        self.assertTrue(hasattr(my_model, "id"))
        self.assertEqual(type(my_model.id), str)
        # created
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertEqual(type(my_model.created_at), datetime)
        # updated
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertEqual(type(my_model.updated_at), datetime)
        # my_number
        self.assertTrue(hasattr(my_model, "my_number"))
        self.assertEqual(type(my_model.my_number), int)
        # name
        self.assertTrue(hasattr(my_model, "name"))
        self.assertEqual(type(my_model.name), str)
        my_model.save()
        my_model_json = my_model.to_dict()
        # checking return being a dict and datetimes to str and __class__
        self.assertTrue((type(my_model_json)) == dict)
        self.assertEqual(type(my_model_json['created_at']), str)
        self.assertIsInstance(my_model_json['updated_at'], str)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        # checking saves correctly and updates updated_at attr
        my_model.name = "Santiago"
        my_model.save()
        sec_json = my_model.to_dict()
        self.assertNotEqual(my_model_json['name'], sec_json['name'])
        self.assertNotEqual(my_model.created_at, my_model.updated_at)
        self.assertEqual(my_model_json['created_at'], sec_json['created_at'])
        new_obj = BaseModel(**sec_json)
        new_obj.save()
        new_json = new_obj.to_dict()
        self.assertDictEqual(sec_json, new_json)
