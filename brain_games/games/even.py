from random import randint


GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def get_game():
    number = randint(1, 999)
    question = f'Question: {number}'
    correct_answer = is_even(number)
    return question, correct_answer
