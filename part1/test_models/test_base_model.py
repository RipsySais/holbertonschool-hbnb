import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.obj = BaseModel()

    def test_initialization(self):
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.created_at, datetime)
        self.assertIsInstance(self.obj.updated_at, datetime)

    def test_save_updates_timestamp(self):
        old_updated = self.obj.updated_at
        self.obj.save()
        self.assertNotEqual(old_updated, self.obj.updated_at)

    def test_to_dict_structure(self):
        obj_dict = self.obj.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
