from brain_games.cli import welcome_user
from brain_games.games.even import even
from brain_games.games.calc import calc
from brain_games.games.mygcd import mygcd
from brain_games.games.progression import progression
from brain_games.games.prime import prime


def brain_go(game, task):
    name = welcome_user()
    counter = 0
    res = 1
    print(task)
    while counter < 3 and res != 0:
        if game == 'even':
            res = even()
        elif game == 'calc':
            res = calc()
        elif game == 'gcd':
            res = mygcd()
        elif game == 'progression':
            res = progression()
        elif game == 'prime':
            res = prime()
        counter += 1
    if counter == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
