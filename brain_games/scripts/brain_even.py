#!/usr/bin/env python

from brain_games.game_general import run_game, ROUNDS_TO_WIN
from brain_games.cli import welcome_user
from brain_games.games.even import generate_question, GAME_RULES


def main():
    name = welcome_user()
    print(GAME_RULES)
    run_game(__import__('brain_games.games.even'), name, rounds=ROUNDS_TO_WIN)


if __name__ == "__main__":
    main()
