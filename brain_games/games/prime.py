from random import randint


GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_start():
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
    return question, correct_answer
