#!/usr/bin/python3
"""
    The file storage module
"""


class FileStorage():
    """
        This module handles file storage
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
            Returns the "__objects" dictionary
        """
        return self.__objects

    def new(self, obj):
        """
            Sets in "__objects" the "obj" with key "<obj class_name>.id"
        """
        key = "{}.{}".format(obj.__class.__name__, obj.id)
        return self.__objects[key] = obj

    def save(self):
        """
            Serializes "__objects" to json file (path: __file_path)
        """

