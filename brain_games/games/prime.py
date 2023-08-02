from random import randint


GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True


def get_game():
    number = randint(1, 99)
    question = f'Question: {number}'
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer
