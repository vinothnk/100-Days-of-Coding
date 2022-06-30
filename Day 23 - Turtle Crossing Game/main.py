import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player1 = Player()
cars = CarManager()
score_board = ScoreBoard()

screen.listen()
screen.onkey(player1.up, "Up")
screen.onkey(player1.down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    score_board.update_scoreboard()
    cars.create_car()
    cars.move_car()

    for car in cars.all_cars:
        if car.distance(player1) < 20:
            game_is_on = False

    if player1.reached_top():
        player1.is_at_top()
        score_board.point_increase()
        cars.level_up()

