from random import randint, choice


GAME_TASK = 'What is the result of the expression?'


def game_start():
    number1 = randint(1, 99)
    number2 = randint(1, 99)
    oper = choice(["+", "-", "*"])
    question = f'Question: {number1} {oper} {number2}'
    if oper == '+':
        correct_answer = number1 + number2
    elif oper == '-':
        correct_answer = number1 - number2
    elif oper == '*':
        correct_answer = number1 * number2
    return question, correct_answer
