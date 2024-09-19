from car import Car
import random


class Cars:
    def __init__(self):
        self.cars = []

        for _ in range(random.randint(5, 9)):
            self.cars.append(Car())

    def move(self):
        for car in self.cars:
            car.move()
