#!/usr/bin/env python

from brain_games.game_general import run_game, ROUNDS_TO_WIN
from brain_games.cli import welcome_user
from brain_games.games.calc import generate_question, GAME_RULES, is_prime


def main():
    print(GAME_RULES)
    name = welcome_user()
    run_game(generate_question, name, rounds=ROUNDS_TO_WIN)


if __name__ == "__main__":
    main()
