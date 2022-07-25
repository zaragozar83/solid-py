from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass


class Square(Shape):

    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side


square = Square(7)
print("The area for the Square is ", square.area())
print("The perimeter for the Square is ", square.perimeter())
