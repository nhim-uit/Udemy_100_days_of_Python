# Udemy: Master Python by building 100 projects in 100 days
# Sep 28, 2024
# Day 25 - US States Game
import turtle
from turtle import Screen
from state import State

import pandas

if __name__ == '__main__':
    screen = Screen()
    screen.bgpic('blank_states_img.gif')
    states = pandas.read_csv('50_states.csv')
    missing_states = states

    user_input = screen.textinput('Guess the State', 'Enter a state\'s name: ').title()

    correct_guess = []
    states_names = states.state.to_list()

    while len(correct_guess) <= 50 and user_input != 'Exit':
        if user_input in states_names \
                and user_input not in correct_guess:
            state_name = states[states.state == user_input]
            correct_guess.append(state_name.state.item())
            s = State(state_name.state.item(), state_name.x.item(), state_name.y.item())
            missing_states = missing_states[missing_states.state != state_name.state.item()]

        if len(correct_guess) == 50:
            break

        user_input = screen.textinput(f'{len(correct_guess)}/50 States Correct', 'Enter another state: ').title()

    missing_states.state.to_csv('missing_states.csv')

    screen.exitonclick()
