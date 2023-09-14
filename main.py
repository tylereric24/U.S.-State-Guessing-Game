from turtle import *
from scoreboard import Scoreboard
from mapwriter import Mapwriter
import pandas as pd
import os

torto = Turtle()
torty = Scoreboard()
tortuga = Mapwriter()

screen = Screen()

data = pd.read_csv("50_states.csv")
answers = data.state.to_list()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

torto.shape(image)

correct_guesses = []

while len(correct_guesses) < 50:

    answer_state = screen.textinput(title="""Guess the State""", prompt="Whats another state's name?\n Stuck? Type 'Exit' to give up").title()

    
    if answer_state == "Exit":
        states_to_learn = []
        for state in answers:
            if state not in correct_guesses:
                states_to_learn.append(state)
        print(f"States to learn {states_to_learn}")
        new_data = pd.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in answers:
        os.system('clear')
        state_data = data[data.state == answer_state]
        x = int(state_data.x)
        y = int(state_data.y)
        tortuga.write_state(x,y,state_data.state.item())
        torty.correct_answer()
        correct_guesses.append(answer_state)
        print(f"Current correct guesses:{correct_guesses}")
    
else:
    print("CONGRATS YOU WIN!")





screen.exitonclick()