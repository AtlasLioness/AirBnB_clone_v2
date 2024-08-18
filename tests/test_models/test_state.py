#!/usr/bin/python3
"""Test cases for State class"""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Test cases for State class"""

    def __init__(self, *args, **kwargs):
        """The Constructor"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Test name attribute of State"""
        new = self.value()
        self.assertEqual(type(new.name), str)
