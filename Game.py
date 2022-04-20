from turtle import Turtle,Screen
from paddle import Paddles_right
from ball import Ball
import time
from paddle_game_scoreboard import Scoreboard
import asyncio
import os
from playsound import playsound
import winsound


#Create and set the screen
screen = Screen()
screen.setup(1400,1000)
screen.title("PONG")
screen.bgcolor('black')
screen.tracer(0)

#Create paddle objects for each player
paddle_right = Paddles_right((650,0))
paddle_left = Paddles_right((-650,0))

#Create new game
# game = Game()

#Create a control panel for each paddle
screen.listen()
screen.onkeypress(key="Up" ,fun = paddle_right.move_UP)
screen.onkeypress(key="Down", fun=paddle_right.move_Down)
screen.onkeypress(key="w" ,fun = paddle_left.move_UP)
screen.onkeypress(key="s", fun=paddle_left.move_Down)
#$screen.onkeypress(key="x",fun=game.start_game)
#creating a ball object
ball=Ball()

#Testing ball object
# test = Turtle()
# test.shape('circle')
# test.color('White')
# test.goto(650,300)
# test.setheading(90)

#Creating a scoreboard object
scoreboard = Scoreboard()

game = True
#Main loop


while game:

    # test.forward(10)
    time.sleep(0.025)
    screen.update()
    ball.move()
    #playsound("epicness.mp3",False)
    #Check the ball distance to the wall
    if ball.ycor()>480 or ball.ycor()<-480:
        ball.bounce_y()
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    # detect a collision with right paddle
    if ball.distance(paddle_right) < 100 and ball.xcor() > 620 or ball.distance(paddle_left)<100 and ball.xcor()<-620:
        ball.bounce_x()
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if ball.xcor() > 680:
        scoreboard.add_player2_score()
        time.sleep(0.5)
        ball.setposition(0,0)

    elif ball.xcor() <-680:
        scoreboard.add_player1_score()
        time.sleep(0.5)
        ball.setposition(0, 0)

    else:
        pass
    if scoreboard.score_player1 == 5 or scoreboard.score_player2 ==5:
        scoreboard.end_of_game_scoreboard()
        game=False
        playsound("mixkit-player-losing-or-failing-2042.wav")
        winsound.PlaySound(None, winsound.SND_ASYNC)
screen.exitonclick()

