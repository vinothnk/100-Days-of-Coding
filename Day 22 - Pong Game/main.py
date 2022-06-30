from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# TODO: 1. create screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)



# TODO: 2. create and move a paddle

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# TODO: 3: create a ball

ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# TODO: scoreboard

score = ScoreBoard()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()
    score.update_scoreboard()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect if r paddle misses the ball
    if ball.xcor() > 380 :
        ball.reset_position()
        score.l_point()

    # detect if l paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()