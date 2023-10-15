#!/usr/bin/python3
import json
"""Defines a base model class."""


class Base:
    """class representing a base object with an optional unique ID."""

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    def to_json_string(list_dictionaries):
        
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        
        else:
            return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        
        if list_objs is None:
            list_objs = []
        
        file_name = cls.__name__ + ".json"
        
        dictionary_list = [obj.to_dictionary() for obj in list_objs]
        
        json_string = cls.to_json_string(dictionary_list)
        
        with open(file_name, "w") as file:
            file.write(json_string)
            
    def from_json_string(json_string):
        
        if json_string is None or len(json_string) == 0:
            return []
        
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ loads instance from dictionary """

        if cls.__name__ == "Rectangle":
            new_ins = cls(1, 1)

        elif cls.__name__ == "Square":
            new = cls(1)

        new_ins.update(**dictionary)
        return new_ins  
    
    @classmethod
    def load_from_file(cls):
        """  returns a list of instances """
        try:
            instance_list = []
            with open(cls.__name__ + ".json", mode='r') as a_file:
                j_file = cls.from_json_string(a_file.read())
                for dic in j_file:
                    instance_list.append(cls.create(**dic))
                return instance_list
        except:
            return []
