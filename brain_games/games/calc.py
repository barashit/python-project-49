#!/usr/bin/env python

import random


GAME_RULES = 'What is the result of the expression?'


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    question = f"{num1} {operation} {num2}"
    correct_answer = str(eval(f"{num1} {operation} {num2}"))
    return question, correct_answer
