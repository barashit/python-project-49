# brain_games/cli.py

import prompt


class GameCLI:
    def __init__(self):
        self.user_name = ""

    def welcome_user(self):
        print("Welcome to the Brain Games!")
        self.user_name = prompt.string('May I have your name? ')
        print(f"Hello, {self.user_name}!")

    def get_user_name(self):
        print(self.user_name)
