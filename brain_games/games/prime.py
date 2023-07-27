from brain_games.cli import answer_dialog
from random import randint


def prime():
    number = randint(0, 99)
    question = f'Question: {number}'
    if number < 2:
        correct_answer = 'no'
    for i in range(2, (number // 2) + 2):
        if number % i == 0:
            correct_answer = 'no'
            break
        else:
            correct_answer = 'yes'
    return answer_dialog(question, correct_answer)
