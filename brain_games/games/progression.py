from brain_games.cli import answer_dialog
from random import randint


def progression():
    left_border = randint(1, 10)
    iterate = randint(1, 10)
    progr_range = randint(5, 10)
    excluded = randint(0, progr_range - 1)
    right_border = left_border + (progr_range - 1) * iterate
    numbers = list(range(left_border, right_border + iterate, iterate))
    question = 'Question:'
    for (i, elem) in enumerate(numbers):
        if i != excluded:
            question += f' {elem}'
        else:
            question += ' .. '
    correct_answer = numbers[excluded]
    return answer_dialog(question, correct_answer)
