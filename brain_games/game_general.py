def run_game(generate_round_data, rounds=5):

    for _ in range(rounds):
        question, correct_answer = generate_round_data()
        print(f"Question: {question}")

        user_answer = input("Your answer: ").strip().lower()

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;. "
                f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again!")
            return

    print(f"Congratulations!")
