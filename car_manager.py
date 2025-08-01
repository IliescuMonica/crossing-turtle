
from turtle import Turtle
from random import *

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def create_car(self):
        random_chance=randint(1,6)
        if random_chance==1:
            new_car = Turtle("square")
            new_car.shapesize(1, 1.5)
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.goto(300, randint(-250, 250))

            self.all_cars.append(new_car)


    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
            self.car_speed += MOVE_INCREMENT

