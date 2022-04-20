import time
from turtle import Turtle


upper_wall_position = 500
lower_wall_position = -500

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.y = input("Chose ball color:\n")
        self.color(f'{self.y}')
        time.sleep(5)
        self.width(20)
        self.penup()
        self.x_move = 15
        self.y_move = 15


    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move =self.y_move*(-1)

    def bounce_x(self):
        self.x_move = self.x_move*(-1)
