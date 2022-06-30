import turtle
from turtle import Turtle

# creating 2 different objects from the same CLASS
tim = Turtle()
tom = Turtle()

tim.color('green')
# state of tim.color attribute is green
tim.forward(100)

tom.color('red')
# state of tom.color attribute is red
tom.back(100)

turtle.exitonclick()
