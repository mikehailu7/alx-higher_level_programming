#!/usr/bin/python3
# Author: MikiasHailu
# Project: Json
""" This is a student class withe init and to json fucntions """


class Student:
   """ This is the declaration of the student class """

    def __init__(self, first_name, last_name, age):
        """ This function will represent the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ This function will return the meaning"""
        return self.__dict__
