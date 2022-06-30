import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)

screen.listen()  # asking the screen object to listen for events
# for object to listen, need event listener. example: turtle.onkey(), turtle.onkeypress()
screen.onkey(key="space", fun=move_forward) # -> look at this. passing a function into another function.
# refer below for example


screen.exitonclick()

# def calculator(n1, n2, func):
    # return func(n1, n2)

# result = calculator(2, 3, add) -> add is the function acting as the 3rd input.
