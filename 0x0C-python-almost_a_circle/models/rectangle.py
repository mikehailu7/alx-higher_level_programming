#!/usr/bin/python3
# Author: MikiasHailu
# Project: Circle
""" This class is ther rectangle class """
from models.base import Base


class Rectangle(Base):
    """ This class have different fuctnions that Represent the rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ This fucnton will Initialize a new Rectangle """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """ This function will Set the height of the Rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """  THis function will rais an error if the height is less than 0  """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """ This function will get the width of the Rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ THis function will rais an error if the width is less than 0 """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def y(self):
        """ This fucntion will get the y postion of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """ THis function will rais an error if the postion is less than 0 """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def x(self):
        """ This fucntion will get the x postion of the rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """ THis function will rais an error if the postion is less than 0 """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def area(self):
        """ This function will Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """ Thsi fucntion will Print the Rectangle using character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """ This fucnction will update the Rectangle """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def __str__(self):
        """ This fucntion will Return the print() and str() of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.x, self.y,
                self.width, self.height)

        def to_dictionary(self):
            """ This fuctnion will Return the body of a Rectangle."""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
