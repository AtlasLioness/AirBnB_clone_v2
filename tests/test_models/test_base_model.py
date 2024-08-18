#!/usr/bin/python3
"""Test cases for BaseModel class"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def __init__(self, *args, **kwargs):
        """The Constructor"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """The Set up test environment"""
        pass

    def tearDown(self):
        """The Clean up after each test"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """The Test default initialization of BaseModel instance"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """The Test initialization of BaseModel instance with kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Test initialization of BaseModel instance with integer kwargs"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save method of BaseModel"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test string representation of BaseModel"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """Test to_dict method of BaseModel"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Test initialization of BaseModel instance with None kwargs"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    @unittest.skip
    def test_kwargs_one(self):
        """Test initialization of BaseModel instance with one kwargs"""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """Test id attribute of BaseModel"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test created_at attribute of BaseModel"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    @unittest.skip
    def test_updated_at(self):
        """Test updated_at attribute of BaseModel"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
