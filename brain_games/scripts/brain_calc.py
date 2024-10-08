import random
from brain_games.game_general import run_game

GAME_RULES = 'What is the result of the expression?'

def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    question = f"{num1} {operation} {num2}"
    correct_answer = str(eval(f"{num1} {operation} {num2}"))
    return question, correct_answer


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ").strip()
    print(f"Hello, {name}!")
    print(GAME_RULES)
    run_game(generate_question)


if __name__ == "__main__":
    main()
