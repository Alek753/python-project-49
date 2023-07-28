from random import randint


GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_start():
    number = randint(1, 999)
    question = f'Question: {number}'
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
