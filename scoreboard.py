from turtle import *
from playsound import playsound


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(500)
        self.current_score = 0
        self.goto(255, -265)
        self.write(f"Current Score:{self.current_score}", font=("Arial", 14))


    
    def update_scoreboard(self):
        self.clear()
        self.goto(255, -265)
        self.write(f"Current Score:{self.current_score}", font=("Arial", 14))


    def correct_answer(self):
        playsound("correct.mp3")
        self.current_score += 1
        self.update_scoreboard()
