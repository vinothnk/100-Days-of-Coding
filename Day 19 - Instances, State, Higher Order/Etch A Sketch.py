from turtle import Turtle, Screen

# TODO: W = forwards, S = backwards, A = counter clockwise, D = clockwise, C = clear and back to center
# create individual functions for each direction and clear screen.

def forwards():
    tim.forward(10)

def backwards():
    tim.back(10)

def counter_clockwise():
    heading_left = tim.heading() + 10
    tim.setheading(heading_left)

def clockwise():
    heading_right = tim.heading() - 10
    tim.setheading(heading_right)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

tim = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="w".lower(), fun=forwards)
screen.onkey(key="s".lower(), fun=backwards)
screen.onkey(key="a".lower(), fun=counter_clockwise)
screen.onkey(key="d".lower(), fun=clockwise)
screen.onkey(key="c".lower(), fun=clear)

screen.exitonclick()

