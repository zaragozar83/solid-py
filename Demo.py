
from abc import ABC, abstractmethod


class Computer(ABC):

    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("It is working")


class Whiteboard(Computer):
    def process(self):
        print("Writing")


class Programmer:
    def work(self, com):
        print("Solving Bugs")
        com.process()


com = Laptop()
com2 = Whiteboard()

prog1 = Programmer()
prog1.work(com2)

prog2 = Programmer()
prog2.work(com)