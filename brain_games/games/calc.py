from random import randint, choice


GAME_TASK = 'What is the result of the expression?'


def calculate_expression(number1, number2, random_operator):
    if random_operator == '+':
        return number1 + number2
    elif random_operator == '-':
        return number1 - number2
    elif random_operator == '*':
        return number1 * number2


def get_game():
    number1 = randint(1, 99)
    number2 = randint(1, 99)
    random_operator = choice(["+", "-", "*"])
    question = f'Question: {number1} {random_operator} {number2}'
    correct_answer = calculate_expression(number1, number2, random_operator)
    return question, str(correct_answer)
