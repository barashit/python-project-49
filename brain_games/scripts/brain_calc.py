#!/usr/bin/env python


import random
from brain_games.game_general import run_game
from brain_games.cli import welcome_user

ROUNDS_TO_WIN = 3
GAME_RULES = 'What is the result of the expression?'


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    question = f"{num1} {operation} {num2}"
    correct_answer = str(eval(f"{num1} {operation} {num2}"))
    return question, correct_answer


def main():
    name = welcome_user()
    print(GAME_RULES)
    run_game(generate_question, name, rounds=ROUNDS_TO_WIN)


if __name__ == "__main__":
    main()
