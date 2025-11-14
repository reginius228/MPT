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


    known_indices = [i for i, x in enumerate(progression) if x is not None]
    first = known_indices[0]
    second = known_indices[1]
    step = (progression[second] - progression[first]) // (second - first)

    return progression[first] + (hidden_index - first) * step
