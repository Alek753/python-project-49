from random import randint


GAME_TASK = 'What number is missing in the progression?'


def generate_numbers():
    left_border = randint(1, 10)
    iterate = randint(1, 10)
    progression_range = randint(5, 10)
    right_border = left_border + (progression_range - 1) * iterate
    return list(range(left_border, right_border + iterate, iterate))


def get_question(numbers, excluded):
    question = 'Question:'
    for (i, elem) in enumerate(numbers):
        if i != excluded:
            question += f' {elem}'
        else:
            question += ' ..'
    return question


def get_game():
    numbers = generate_numbers()
    excluded = randint(0, len(numbers))
    correct_answer = numbers[excluded]
    question = get_question(numbers, excluded)
    return question, str(correct_answer)
