from brain_games.cli import answer_dialog
from random import randint
import random


def calc():
    number1 = randint(1, 99)
    number2 = randint(1, 99)
    oper = random.choice(["+", "-", "*"])
    question = f'Question: {number1} {oper} {number2}'
    if oper == '+':
        correct_answer = number1 + number2
    elif oper == '-':
        correct_answer = number1 - number2
    elif oper == '*':
        correct_answer = number1 * number2
    return answer_dialog(question, correct_answer)
