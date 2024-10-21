#!/usr/bin/env python3


from brain_games.cli import welcome_user
from brain_games.games import even  # Убедитесь, что импорт правильный

if __name__ == "__main__":
    name = setup_game(even)  # Передаем модуль even
    run_game(even, name)
