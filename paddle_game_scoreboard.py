from turtle import Turtle
from playsound import playsound

class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score_player1 = 0
        self.score_player2 = 0
        self.hideturtle()
        self.color('White')
        self.penup()
        self.goto(-40,450)
        self.write(f'Score {self.score_player1}:{self.score_player2}', font=('Arial', 20, 'normal'))


    def add_player1_score(self):
        self.score_player1+=1
        self.clear()
        self.write(f'Score {self.score_player1}:{self.score_player2}', font=('Arial', 20, 'normal'))

    def add_player2_score(self):
        self.score_player2+=1
        self.clear()
        self.write(f'Score {self.score_player1}:{self.score_player2}', font=('Arial', 20, 'normal'))

    def end_of_game_scoreboard(self):
        if self.score_player1==5:
            self.clear()
            self.write("RIGHT PLAYER WON!", font=('Arial', 20, 'normal'))
        elif self.score_player2==5:
            self.clear()
            self.write(("LEFT PLAYER WON!"), font=('Arial', 20, 'normal'))
