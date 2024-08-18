#!/usr/bin/python3
"""Test cases for City class"""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """Test cases for City class"""

    def __init__(self, *args, **kwargs):
        """The constructor"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test state_id attribute of City"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Test name attribute of City"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    @unittest.skip
    def test_population(self):
        """Test population attribute of City"""
        new = self.value()
        self.assertIsNone(new.population)
