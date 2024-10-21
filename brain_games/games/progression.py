import random


GAME_RULES = 'What number is missing in the progression?'


def generate_progression():
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    length = 10

    progression = [start + step * i for i in range(length)]
    missing_index = random.randint(0, length - 1)

    correct_answer = str(progression[missing_index])
    progression[missing_index] = '..'
    question = ' '.join(map(str, progression))

    return question, str(correct_answer)
