import random
import math

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def generate_question():
    return random.randint(2, 100)

def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def get_correct_answer(question):
    return "yes" if is_prime(question) else "no"
