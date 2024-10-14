#!/usr/bin/env python


import random
from brain_games.game_general import run_game
from brain_games.cli import welcome_user

ROUNDS_TO_WIN = 3
GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

def is_even(number):
    return number % 2 == 0

def generate_question():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer

def main():
    name = welcome_user()
    print(GAME_RULES)
    run_game(generate_question, name, rounds=ROUNDS_TO_WIN)

if __name__ == "__main__":
    main()
