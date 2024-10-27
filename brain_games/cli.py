# brain_games/cli.py

import prompt

class GameCLI:
    def __init__(self):
        self.user_name = ""


def welcome_user():
    global user_name
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")
