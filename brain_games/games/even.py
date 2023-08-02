from random import randint


GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_game():
    number = randint(1, 999)
    question = f'Question: {number}'
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer
