import prompt

MAX_ROUNDS = 3

def run_game(description: str, generate_question, get_correct_answer):
    print("Welcome to the VD-games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(description)

    correct_count = 0
    while correct_count < MAX_ROUNDS:
        question = generate_question()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ").strip().lower()

        correct_answer = str(get_correct_answer(question)).lower()
        if user_answer == correct_answer:
            print("Correct!")
            correct_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
