#!/usr/bin/env python3

from brain_games.games import gcd
from brain_games.game_general import run_game, setup_game


def main():
    name = setup_game(gcd)
    run_game(gcd, name)


if __name__ == "__main__":
    main()
