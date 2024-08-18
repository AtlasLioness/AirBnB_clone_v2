#!/usr/bin/python3
"""Test cases for Amenity class"""
from datetime import datetime
import models
from models.base_model import BaseModel
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Test cases for Amenity class"""

    def __init__(self, *args, **kwargs):
        """The constructor"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test name attribute of Amenity"""
        new = self.value()
        self.assertEqual(type(new.name), str)
