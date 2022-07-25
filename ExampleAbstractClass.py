from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def go(self):
        print("Your drive the car")

    def stop(self):
        print("Stop car")


class Motorcycle(Vehicle):

    def go(self):
        print("Your ride the motorcycle")

    def stop(self):
        print("Motorcycle stopped")


car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()

car.stop()
motorcycle.stop()
