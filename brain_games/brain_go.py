from brain_games.cli import welcome_user
from brain_games.games.even import even
from brain_games.games.calc import calc
from brain_games.games.mygcd import mygcd
from brain_games.games.progression import progression
from brain_games.games.prime import prime


def brain_go(game):
    name = welcome_user()
    counter = 0
    res = 1
    while counter < 3 and res != 0:
        if game == 'even':
            if counter == 0:
                print('Answer "yes" if the number is even,'
                      ' otherwise answer "no".')
            res = even()
        elif game == 'calc':
            if counter == 0:
                print('What is the result of the expression?')
            res = calc()
        elif game == 'gcd':
            if counter == 0:
                print('Find the greatest common divisor of given numbers.')
            res = mygcd()
        elif game == 'progression':
            if counter == 0:
                print('What number is missing in the progression?')
            res = progression()
        elif game == 'prime':
            if counter == 0:
                print('Answer "yes" if given number is prime.'
                      ' Otherwise answer "no".')
            res = prime()
        counter += 1
    if counter == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
