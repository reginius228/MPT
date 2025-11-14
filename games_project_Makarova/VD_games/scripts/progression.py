import random

DESCRIPTION = "What number is missing in the progression?"

def generate_question():
    start = random.randint(1, 20)
    step = random.randint(1, 5)
    length = random.randint(5, 15)
    hidden_index = random.randint(0, length - 1)
    progression = [start + i * step for i in range(length)]
    question = " ".join(str(num) if i != hidden_index else ".." for i, num in enumerate(progression))
    return question

def get_correct_answer(question):
    parts = question.split()
    progression = [int(p) if p != ".." else None for p in parts]
    hidden_index = progression.index(None)
    step = (progression[hidden_index + 1] - progression[hidden_index - 1]) // 2 if hidden_index > 0 and hidden_index < len(progression) - 1 else \
           progression[1] - progression[0]
    return progression[0] + hidden_index * step
