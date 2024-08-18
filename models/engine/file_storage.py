#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {"BaseModel": BaseModel, "User": User, "Place": Place,
           "State": State, "City": City, "Amenity": Amenity,
           "Review": Review}


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            new_dict = {}
            for k, v in self.__objects.items():
                if cls == v.__class__ or cls == v.__class__.__name__:
                    new_dict[k] = v
            return new_dict
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj is not None:
            k = obj.__class__.__name__ + "." + obj.id
            self.__objects[k] = obj

    def save(self):
        """Saves storage dictionary to file"""
        json_objects = {}
        for k in self.__objects:
            json_objects[k] = self.__objects[k].to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r') as f:
                re = json.load(f)
            for k in re:
                self.__objects[k] = classes[re[k]['__class__']](**re[k])
        except:
            pass

    def delete(self, obj=None):
        """delets obj from __objects"""
        if obj is not None:
            k = obj.__class__.__name__ + '.' + obj.id
            if k in self.__objects:
                del self.__objects[k]

    def close(self):
        """calls reload() for JSON deserialization"""
        self.reload()
