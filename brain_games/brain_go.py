import prompt
from brain_games.games.even import even
from brain_games.games.calc import calc
from brain_games.games.mygcd import mygcd
from brain_games.games.progression import progression
from brain_games.games.prime import prime


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def brain_go(game, task):
    name = welcome_user()
    counter = 0
    result = 1
    print(task)
    while counter < 3 and result != 0:
        if game == 'even':
            result = even()
        elif game == 'calc':
            result = calc()
        elif game == 'gcd':
            result = mygcd()
        elif game == 'progression':
            result = progression()
        elif game == 'prime':
            result = prime()
        counter += 1
    if counter == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
