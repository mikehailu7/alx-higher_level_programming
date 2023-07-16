#!/usr/bin/python3
# Author: MikiasHailu
# Project: Circle
""" This is the square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ This class have different fuctnions that Represent the square rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ This fucnton will Initialize a new Rectangle """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ This fucntion will get the size """
        return self.width

    @size.setter
    def size(self, value):
        """ This fucntion will get the size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ This fucntion will update the square rectangle """
        if args and len(args) != 0:
            m = 0
            for arg in args:
                if m == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif m == 1:
                    self.size = arg
                elif m == 2:
                    self.x = arg
                elif m == 3:
                    self.y = arg
                m = m + 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def __str__(self):
        """ This function will Return the print() and str() representation of a Square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)


    def to_dictionary(self):
        """ This fucntion will return the dictionary representation of the Square """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
            }
