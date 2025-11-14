import random

def generate_expression():
    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    operator = random.choice(['+', '-', '*'])
    expression = f"{num1} {operator} {num2}"
    if operator == '+':
        correct = num1 + num2
    elif operator == '-':
        correct = num1 - num2
    else:
        correct = num1 * num2
    return expression, str(correct)

def play_game():
    print("Welcome to the VD-games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

    correct_answers = 0
    while correct_answers < 3:
        question, correct_answer = generate_expression()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    play_game() 
