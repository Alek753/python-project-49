from random import randint


GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return 'no'
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return 'no'
            break
    return 'yes'


def get_game():
    number = randint(1, 99)
    question = f'Question: {number}'
    correct_answer = is_prime(number)
    return question, correct_answer
