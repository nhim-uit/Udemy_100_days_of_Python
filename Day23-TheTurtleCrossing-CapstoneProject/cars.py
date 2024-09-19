from car import Car
from CONSTANTS import NO_OF_CARS


class Cars:
    def __init__(self):
        self.__cars = []

        for _ in range(NO_OF_CARS):
            self.__cars.append(Car())

    def move(self):
        for car in self.__cars:
            car.move()

    def get_cars(self):
        return self.__cars
