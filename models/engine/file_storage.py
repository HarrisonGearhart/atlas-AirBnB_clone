#!/usr/bin/python3
"""Module for FileStorage class
serializes instances to a JSON file and deserializes JSON file to instances"""
import json
from models.base_model import BaseModel

class FileStorage:
    """
    Class for storing and retrieving data
    Private class attributes:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all objects
        by <class name>.id
        (ex: to store a BaseModel object with id=12121212,
        the key will be BaseModel.12121212)
    Public instance methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
    """
    def __init__(self):
        self._FileStorage__file_path = "file.json"
        self._FileStorage__objects = {}

    def all(self):
        return self._FileStorage__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self._FileStorage__objects[key] = obj

    def save(self):
        dict = {}
        for key, value in self._FileStorage__objects.items():
            dict[key] = value.to_dict()
        with open(self._FileStorage__file_path, "w") as file:
            json.dump(dict, file)

    def reload(self):
        try:
            with open(self._FileStorage__file_path, "r") as file:
                obj_list = json.load(file)
                for key, value in obj_list.items():
                    string = key.split(".")
                    obj = eval(string[0])(**value)
                    self._FileStorage__objects[key] = obj

        except Exception:
            pass
