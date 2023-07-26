from brain_games.cli import answer_dialog
from random import randint
from math import gcd


def mygcd():
    number1 = randint(1, 99)
    number2 = randint(1, 99)
    correct_answer = gcd(number1, number2)
    question = f'Question: {number1} {number2}'
    return answer_dialog(question, correct_answer)
