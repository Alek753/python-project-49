import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I hace your name? ')
    print(f'Hello, {name}!')


def answer_dialog(question, correct_answer):
    print(question)
    user_answer = prompt.string('Your answer: ')
    if user_answer == str(correct_answer):
        print('Correct!')
        return 1
    else:
        print(f"'{user_answer}' is wrong answer ;(."
              f" Correct answer was '{correct_answer}'.")
        return 0
