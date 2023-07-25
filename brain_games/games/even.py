from brain_games.cli import answer_dialog
from random import randint


def even():
    number = randint(1, 999)
    question = f'Question: {number}'
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return answer_dialog(question, correct_answer)
