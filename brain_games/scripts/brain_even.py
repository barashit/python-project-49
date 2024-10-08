import random
from brain_games.game_general import run_game

ROUNDS_TO_WIN = 5
GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

def is_even(number):
    return number % 2 == 0

def generate_question():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer

def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ").strip()
    print(f"Hello, {name}!")
    print(GAME_RULES)
    run_game(generate_question)

if __name__ == "__main__":
    main()
