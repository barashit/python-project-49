import random
from brain_games.game_general import run_game

GAME_RULES = 'Answer "yes" if the number is prime, otherwise answer "no".'

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_question():
    question = random.randint(1, 100)
    correct_answer = "yes" if is_prime(question) else "no"
    return question, correct_answer


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ").strip()
    print(f"Hello, {name}!")
    print(GAME_RULES)
    run_game(generate_question)


if __name__ == "__main__":
    main()
