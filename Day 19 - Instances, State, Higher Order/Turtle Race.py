import turtle
from turtle import Turtle, Screen
import random

screen = Screen()

is_race_on = False
# setting up the screen size.
screen.setup(width=500, height=400)
# asking user for their input
user_bet = screen.textinput(title='Make your bet.', prompt='Which turtle will win the race? Enter your color: ')
colors = ['red', 'blue', 'green', 'purple', 'orange', 'yellow']
all_turtles = []
y_position = [-150, -100, -50, 0, 50, 100]


# how to give x and y coordinates
# centre = 0, 0
# so divide the screen.setup() into 2. then move accordingly.
# tim.penup()
# tim.goto(x=-230, y=-100)

# make the turtle to go the start of the line -> left of window
# create turtles using for loop
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for selected_turtle in all_turtles:
        if selected_turtle.xcor() > 230:
            is_race_on = False
            winning_color = selected_turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won. The {winning_color} turtle has won!")
            else:
                print(f"You have lost. The {winning_color} turtle has won!")
        random_distance = random.randint(0, 10)
        selected_turtle.forward(random_distance)









screen.exitonclick()

