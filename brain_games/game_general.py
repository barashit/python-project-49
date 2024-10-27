from brain_games.cli import welcome_user
from cli import welcome_user, user_name


ROUNDS_TO_WIN = 3


def run_game(game_module, rounds=ROUNDS_TO_WIN):
    welcome_user()
    print(game_module.GAME_RULES)

    for _ in range(rounds):
        question, correct_answer = game_module.generate_question()
        print(f"Question: {question}")

        user_answer = input("Your answer: ").strip().lower()

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;. "
                f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            break

    else:
        print(f"Congratulations, {user_name}!")
