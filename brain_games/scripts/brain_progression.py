import random
from brain_games.game_general import run_game

GAME_RULES = 'Answer "yes" if the number is prime, otherwise answer "no".'

def generate_progression():
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    length = random.randint(5, 10)

    progression = [start + step * i for i in range(length)]
    missing_index = random.randint(0, length - 1)

    correct_answer = progression[missing_index]
    progression[missing_index] = '..' 
    question = ' '.join(map(str, progression))   

    return progression, str(correct_answer)


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ").strip()
    print(f"Hello, {name}!")
    print(GAME_RULES)
    run_game(generate_progression) 


if __name__ == "__main__":
    main()
