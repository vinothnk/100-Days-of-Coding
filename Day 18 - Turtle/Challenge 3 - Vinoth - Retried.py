import random
import turtle
from turtle import Turtle

tim = Turtle()
tim.shape('turtle')

pen_colors = ['black', 'blue', 'teal', 'lawn green', 'gold', 'sienna', 'maroon', 'light salmon', 'crimson', 'magenta']

# put shapes in a function
def draw_shape(num_sides):
    angle = round(360 / num_sides, 2)
    for num in range(num_sides):
        tim.left(angle)
        tim.forward(100)

for shape_side_n in range(3, 11):
    tim.color(random.choice(pen_colors))
    draw_shape(shape_side_n)












#shape_side()
select_color()
turtle.exitonclick()