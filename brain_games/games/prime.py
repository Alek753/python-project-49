from random import randint


GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_start():
    number = randint(1, 99)
    question = f'Question: {number}'
    correct_answer = 'yes'
    if number < 2:
        correct_answer = 'no'
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            correct_answer = 'no'
            break
    return question, correct_answer
