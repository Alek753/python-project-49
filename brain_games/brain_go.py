import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


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


def brain_go(game):
    name = welcome_user()
    counter = 0
    result = 1
    print(game.GAME_TASK)
    while counter < 3 and result != 0:
        question, correct_answer = game.game_start()
        result = answer_dialog(question, correct_answer)
        counter += result
    if counter == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
