#!/usr/bin/python3
# Author: MIkiasHailu
# Project: Rectangle
""" This class is called rectangle class """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This is the representation of a rectangle with a parameter baseGeometery """
    def __init__(self, width, height):
        """ THis is the initializaion of the above rectangle"""
        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width
