import turtle

window = turtle.Screen()

# Starting parameters
MAX_X = 300
MAX_Y = 300
initial_angle = 15
speed = 10

# Create a turtle and name it Bob.
Bob = turtle.Turtle()
window.reset()
window.setworldcoordinates(-MAX_X,-MAX_Y,MAX_X,MAX_Y)
Bob.right(initial_angle)
#Bob.fd(51) No need for this
Bob.speed(speed)
while True:
    xBob = Bob.xcor()
    yBob = Bob.ycor()
    print(xBob,yBob)
    if abs(xBob) >= MAX_X: # Use abs() to capture both walls
        heading = Bob.heading()
        print(heading)
        Bob.setheading(180 - heading)
    if abs(yBob) >= MAX_Y:
        heading = Bob.heading()
        Bob.setheading(-heading)
    Bob.fd(1)
window.exitonclick()