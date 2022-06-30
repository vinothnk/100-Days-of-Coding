from turtle import Turtle, Screen

# TODO: W = UP, S = DOWN, A = LEFT, D = RIGHT, C = clear and back to center
# create individual functions for each direction and clear screen.

def up():
    heading_up = tim.heading() + 90
    tim.setheading(heading_up)


def down():
    heading_down = tim.heading() + 0
    tim.setheading(heading_down)

def left():
    heading_left = tim.heading() + 90
    tim.setheading(heading_left)

def right():
    heading_right = tim.heading() + 90
    tim.setheading(heading_right)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def forwards():
    tim.forward(10)

tim = Turtle()
screen = Screen()



game_on = True

while game_on:
    screen.listen()
    screen.onkey(key="w".lower(), fun=up)
    # screen.onkey(key="s".lower(), fun=down)
    screen.onkey(key="a".lower(), fun=left)
    screen.onkey(key="d".lower(), fun=right)
    screen.onkey(key="c".lower(), fun=clear)
    tim.forward(5)

screen.exitonclick()

