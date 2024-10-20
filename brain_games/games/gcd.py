#!/usr/bin/env python

import random

GAME_RULES = 'Find the greatest common divisor of given numbers.'


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    question = f"{num1} {num2}"
    correct_answer = str(math.gcd(num1, num2))

    return question, correct_answer
