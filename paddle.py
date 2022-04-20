from turtle import Turtle

class Paddles_right(Turtle):
    def __init__(self,position):
        super().__init__()

        self.penup()
        self.shape('square')
        self.xd = input("Chose your paddle color: \n")
        self.color(f'{self.xd}')
        self.shapesize(10,1)
        self.goto(position)


    def move_UP(self):
        new_y = self.ycor()+50
        self.goto(self.xcor(),new_y)
    def move_Down(self):
        new_y = self.ycor()-50
        self.goto(self.xcor(), new_y)

