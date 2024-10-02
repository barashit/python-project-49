import random
import math


def welcome_user():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    question = f"{num1} {num2}"
    correct_answer = math.gcd(num1, num2)

    return question, correct_answer


def brain_gcd():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    rounds = 3

    for _ in range(rounds):
        question, correct_answer = generate_question()
        print(f"Question: {question}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    brain_gcd()


if __name__ == "__main__":
    main()
