#!/usr/bin/env python

import random
import math
from brain_games.game_general import run_game
from brain_games.cli import welcome_user

ROUNDS_TO_WIN = 3
GAME_RULES = 'Find the greatest common divisor of given numbers.'

def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    question = f"{num1} {num2}"
    correct_answer = str(math.gcd(num1, num2))

    return question, correct_answer


def main():
    name = welcome_user()
    print(GAME_RULES)
    run_game(generate_question, name, rounds=ROUNDS_TO_WIN)


if __name__ == "__main__":
    main()
