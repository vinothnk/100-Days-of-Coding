import turtle
from turtle import Turtle

tim = Turtle()
tim.shape('turtle')

# triangle
for _ in range(3):
    tim.right(120)
    tim.forward(100)

tim.pencolor('red')

# square
for _ in range(4):
    tim.right(90)
    tim.forward(100)

tim.pencolor('blue')

# pentagon
for _ in range(5):
    tim.right(72)
    tim.forward(100)

tim.pencolor('green')

# hexagon

for _ in range(6):
    tim.right(60)
    tim.forward(100)

tim.pencolor('purple')

# heptagon

for _ in range(7):
    tim.right(51.42)
    tim.forward(100)

tim.pencolor('deep pink')

# octagon

for _ in range(8):
    tim.right(45)
    tim.forward(100)

tim.pencolor('dark blue')

# nonagon

for _ in range(9):
    tim.right(40)
    tim.forward(100)

tim.pencolor('orange')

# decagon

for _ in range(10):
    tim.right(36)
    tim.forward(100)


turtle.exitonclick()