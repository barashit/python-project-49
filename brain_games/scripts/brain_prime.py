#!/usr/bin/env python


from brain_games.cli import welcome_user
from brain_games.games import prime
from brain_games.game_general import run_game, setup_game


def main():
    name = setup_game(prime)
    run_game(prime, name)

if __name__ == "__main__":
    main()
