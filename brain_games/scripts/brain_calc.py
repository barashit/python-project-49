import random


def welcome_user():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    question = f"{num1} {operation} {num2}"
    correct_answer = eval(f"{num1} {operation} {num2}")
    return question, correct_answer


def brain_calc():
    name = welcome_user()
    print("What is the result of the expression?")
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
            print(
                f"'{user_answer}' is wrong answer ;. "
                f"Correct answer was '{correct_answer}'."
            )

            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    brain_calc()


if __name__ == "__main__":
    main()
