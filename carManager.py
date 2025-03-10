import random
import turtle
from turtle import Turtle

COLOR = ["red", "green", "blue", "orange", "purple", "yellow"]

MOVE_BY = 5
MOVE_PLUS = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_BY

    def create_Car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLOR))
            random_y = random.randint(-250,250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_PLUS

