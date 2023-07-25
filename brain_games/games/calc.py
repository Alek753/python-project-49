from brain_games.cli import answer_dialog
from random import randint


def calc():
    number1 = randint(1, 999)
    number2 = randint(1, 999)
    oper = random.choise(["+", "-", "*"])
    question = f'Question: {number1} {oper} {number2}'
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return answer_dialog(question, correct_answer)
