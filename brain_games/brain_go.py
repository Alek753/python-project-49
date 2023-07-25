from brain_games.cli import welcome_user
from brain_games.games.even import even
from brain_games.games.calc import calc


def brain_go(game):
    name = welcome_user()
    counter = 0
    res = 1
    while counter < 3 and res != 0:
        if game == 'even':
            if counter == 0:
                print('Answer "yes" if the number is even, otherwise answer "no".')
            res = even()
        elif game == 'calc':
            if counter == 0:
                print('What is the result of the expression?')
            res = calc()
        counter += 1
    if counter == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")