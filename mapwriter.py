from turtle import *
import pandas as pd



class Mapwriter(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(500)


    def write_state(self, x, y,state):
        self.penup()
        self.setposition(x, y)
        self.pendown()
        self.write(state)





    