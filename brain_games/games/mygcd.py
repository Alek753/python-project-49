from random import randint
from math import gcd


GAME_TASK = 'Find the greatest common divisor of given numbers.'


def game_start():
    number1 = randint(1, 99)
    number2 = randint(1, 99)
    correct_answer = gcd(number1, number2)
    question = f'Question: {number1} {number2}'
    return question, correct_answer
