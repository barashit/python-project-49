import random


def welcome_user():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def generate_progression():
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    length = random.randint(5, 10)

    progression = [start + step * i for i in range(length)]
    missing_index = random.randint(0, length - 1)

    correct_answer = progression[missing_index]
    progression[missing_index] = '..'  # заменяем число на '..'

    return progression, correct_answer


def brain_progression():
    name = welcome_user()
    print("What number is missing in the progression?")
    rounds = 3

    for _ in range(rounds):
        progression, correct_answer = generate_progression()
        print("Question:", ' '.join(map(str, progression)))

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )

            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    brain_progression()


if __name__ == "__main__":
    main()
