#!/usr/bin/python3
# Author: MikiasHailu
# project: Json
""" This is a student class """


class Student:
    """ This class contains init and to json functions """

    def __init__(self, first_name, last_name, age):
        """ This function will Initialize a new Student """
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self, attrs=None):
        """ This funciton will Get the student info """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
