# import another_module
#
# print(another_module.another_variable)
#
# import turtle
#
# timmy = turtle.Turtle()
# #timmy is object
# #class is Turtle()

# another way is below
from turtle import Turtle, Screen

# importing class from turtle

timmy = Turtle()
# timmy is object
# class is Turtle()
# print(timmy)
# timmy.shape("turtle")  # changing shape of timmy
# timmy.color("blue")  # changing color of timmy
# timmy.forward(100)  # moving forward 100 steps
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)

my_screen = Screen()
# new object my_screen from Screen() class
print(my_screen.canvheight)
# my_screen -> object, canvheight -> attribute
# .canvheight -> pulling the attributes inside Screen() class for my_screen object

my_screen.exitonclick()
# calling exitonclick() method from my_screen object
