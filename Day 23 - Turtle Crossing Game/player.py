from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.setheading(90)
        self.speed('fastest')
        self.penup()
        self.setpos(STARTING_POSITION)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.back(MOVE_DISTANCE)

    def is_at_top(self):
        self.goto(STARTING_POSITION)

    def reached_top(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False