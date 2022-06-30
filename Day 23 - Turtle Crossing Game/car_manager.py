import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
all_cars = []


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # creates initial cars
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.penup()
            # stretching the car to a rectangle
            new_car.shapesize(1, 2, 1)
            # random selection of colors of each car
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    # get random cars to move to the left at random speeds
    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
            self.car_speed += MOVE_INCREMENT