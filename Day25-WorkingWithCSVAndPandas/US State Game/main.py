# Udemy: Master Python by building 100 projects in 100 days
# Sep 28, 2024
# Day 25 - US States Game
import turtle
from turtle import Screen
from state import State
from scoreboard import Scoreboard

import pandas

if __name__ == '__main__':
    screen = Screen()
    screen.bgpic('blank_states_img.gif')
    states = pandas.read_csv('50_states.csv')

    user_input = screen.textinput('Guess the State', 'Enter a state\'s name: ')
    count = 50
    score = Scoreboard()

    while count > 48:
        if states.state.str.lower().str.contains(user_input.lower()).any():
            score.increase()
            state_name = states[states.state.str.lower() == user_input.lower()]
            s = State(state_name.state.iloc[0], state_name.x.iloc[0], state_name.y.iloc[0])
            user_input = screen.textinput(f'{score.score}/50 States Correct', 'Enter another state: ')
        else:
            user_input = screen.textinput('Guess the State', 'Re-enter a state: ')

        count -= 1

    score.game_over()
    screen.exitonclick()
