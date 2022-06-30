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

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))

