from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)


starting_position = [(0,0), (-20,0), (-40,0)] # use tuples to lock locations

segments = []
# TODO: create snake body
# create 3 turtles -> make them square shaped. each turtle pixel 20 x 20
# should be white in color

# my version
# for index in range(3):
#     new_turtle = Turtle(shape='square')
#     new_turtle.color('white')
#     new_turtle.penup()
#     new_turtle.goto(x = x_position[index], y = 0)
#     turtles.append(new_turtle)

#angela version

for position in starting_position:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


# moving the snake
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for seg in segments:
    #     seg.forward(20)
    # this allows the snake to move forward only. how to get the body to follow when the head turn?
    # need to use for loop to make segment 3 move to segment 2 position, seg2 to seg 1, seg1 to turn.
    # so making the body go into the different previous positions when the head turns.
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)







screen.exitonclick()