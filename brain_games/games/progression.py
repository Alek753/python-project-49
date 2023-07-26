from brain_games.cli import answer_dialog
from random import randint


def progression():
    left_border = randint(1, 10)
    iterate = randint(1, 10)
    progr_range = randint(5, 10)
    excluded = randint(0, progr_range - 1)
    right_border = left_border + (progr_range - 1) * iterate
    numbers = list(range(left_border, right_border + iterate, iterate))
    print(left_border, right_border, iterate, progr_range, excluded)
    print(numbers)
#    print(numbers[progr_range - 1:progr_range])
    left = numbers[: excluded]
    right = numbers[excluded + 1:]
    print(*left, sep = ' ')
#    print(f'{numbers[: excluded]} {numbers[excluded + 1, progr_range]}')    
#    question = f'Question: {number1} {oper} {number2}'
#    return answer_dialog(question, correct_answer)