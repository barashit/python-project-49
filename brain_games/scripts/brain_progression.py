#!/usr/bin/env python

import random
from brain_games.game_general import run_game
from brain_games.cli import welcome_user

ROUNDS_TO_WIN = 3
GAME_RULES = 'Answer "yes" if the number is prime, otherwise answer "no".'

def generate_progression():
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    length = 10

    progression = [start + step * i for i in range(length)]
    missing_index = random.randint(0, length - 1)

    correct_answer = str(progression[missing_index])
    progression[missing_index] = '..' 
    question = ' '.join(map(str, progression))   

    return question, str(correct_answer)


def main():
    name = welcome_user()
    print(GAME_RULES)
    run_game(generate_progression, name, rounds=ROUNDS_TO_WIN)


if __name__ == "__main__":
    main()
