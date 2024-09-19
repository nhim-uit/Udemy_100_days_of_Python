from car import Car
import random


class Cars:
    def __init__(self):
        self.__cars = []

        for _ in range(random.randint(5, 9)):
            self.__cars.append(Car())

    def move(self):
        for car in self.__cars:
            car.move()

    def get_cars(self):
        return self.__cars
