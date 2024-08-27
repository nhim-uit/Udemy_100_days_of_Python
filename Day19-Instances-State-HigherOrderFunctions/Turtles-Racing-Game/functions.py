from turtle import Screen


def choose_color(screen: Screen) -> str:
    """
    Prompt to ask for user's input of color
    :return: str
    """
    return screen.textinput(title='Make your bet', prompt='Who will win the race? Input a color: ')


def compare(user_color, winning_color):
    if winning_color.lower() == user_color.lower():
        print(f'You\'ve won! The {winning_color} turtle is the winner.')
    else:
        print(f'You\'ve lost! The {winning_color} turtle is the winner.')
