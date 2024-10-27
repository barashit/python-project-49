from brain_games.cli import GameCLI


ROUNDS_TO_WIN = 3


def run_game(game_module, rounds=ROUNDS_TO_WIN):
    cli = GameCLI()
    cli.welcome_user()
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
            print(f"Let's try again, {cli.user_name}!")
            break

    else:
        print(f"Congratulations, {cli.user_name}!")
