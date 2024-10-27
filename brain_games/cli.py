# brain_games/cli.py

import prompt

class GameCLI:
    def welcome_user(self):
        print("Welcome to the Brain Games!")
        user_name = prompt.string('May I have your name? ')
        print(f"Hello, {user_name}!")
