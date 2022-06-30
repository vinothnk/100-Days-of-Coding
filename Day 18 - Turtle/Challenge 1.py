# use turtle to draw a square
import turtle
from turtle import Turtle

timmy = Turtle()
timmy.shape('turtle')
timmy.color('dark violet')

def draw_square():
    for num in range(4):
        timmy.forward(100)
        timmy.right(90)

draw_square()

turtle.exitonclick()