import random
import math
from brain_games.game_general import run_game

GAME_RULES = 'Find the greatest common divisor of given numbers.'

def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    question = f"{num1} {num2}"
    correct_answer = str(math.gcd(num1, num2))

    return question, correct_answer


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ").strip()
    print(f"Hello, {name}!")
    print(GAME_RULES)
    run_game(generate_question)


if __name__ == "__main__":
    main()
