my_tuple = (1, 3, 8)
print(my_tuple)

# tuple items cannot be changed unlike list

my_tuple = list(my_tuple)
print(my_tuple)

# if want to change elements, change tuple to list and change back to tuple.

import turtle as t
import random

tim = t.Turtle()
tim.shape('turtle')

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270, 360]
# TODO: increase thickness of turtle pen
tim.width(5)

# TODO: increase speed of turtle
tim.speed(7)

# TODO: create random directions.
for i in range(100):
    # TODO: create random colors
    tim.color(random.choice(colours))
    tim.forward(50)
    a = random.randrange(0,360,90)
    tim.right(a)

t.exitonclick()

print("_____________________________________________________________")

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
########### Challenge 4 - Random Walk ########
#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = tuple(r,g,b)
    return random_color()

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

