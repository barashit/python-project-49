import random


def welcome_user():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def brain_prime():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    rounds = 3

    for _ in range(rounds):
        question = random.randint(1, 100)
        print(f"Question: {question}")
        correct_answer = "yes" if is_prime(question) else "no"

        user_answer = input("Your answer: ").strip().lower()

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. " +
            f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    brain_prime()


if __name__ == "__main__":
    main()
