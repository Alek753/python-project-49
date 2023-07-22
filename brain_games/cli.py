import prompt

def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I hace your name? ')
    print(f'Hello, {name}!')
