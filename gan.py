#!/usr/bin/env/ python3
"""Guess a random number, or make the computer guess yours!"""

__version__ = '0.2'
__author__ = 'ehlodex'

import random
import time
import os

default_max_tries = int(10)
default_min = random.randint(1, 100)  # or int(1)
default_max = random.randint(default_min+50, default_min+100)  # or int(100)
p1_name = p2_name = os.getlogin()
p_names = ('GERTY', 'TARS', 'Data', 'Wall-E', 'Agent Smith', 'HAL 9000')


def clear():
    print('\n' * 80)  # this is a hack to clear the output in PyCharm
    os.system('cls' if os.name == 'nt' else 'clear')


def reset():
    input('Something went wrong. Press ENTER to try again. ')
    clear()
    main()


def main():
    try:
        players = int(input('How many players? (0-2) ') or 1)
        assert 0 <= players <= 2
    except (ValueError, AssertionError):
        reset()
        return
    p1_ui, p2_ui = set_players(players)
    p1_min, p1_max = set_range(ui=p1_ui)
    p1_num = set_num(p1_min, p1_max, ui=p1_ui)
    print('The epic battle of wits between {} and {} has begun!'
          .format(p1_name, p2_name))
    winner = guess_num(p1_min, p1_max, p1_num, default_max_tries, ui=p2_ui)
    print('Congratulations, {}! You win!'.format(winner))


def set_range(local_min=default_min, local_max=default_max, ui=True):
    if ui:
        local_min = input('min: [{}] '.format(local_min)) or local_min
        local_max = input('max: [{}] '.format(local_max)) or local_max
    try:
        local_min = int(local_min)
        local_max = int(local_max)
        if local_min > local_max:
            local_min, local_max = local_max, local_min
        assert local_min < local_max
    except (ValueError, AssertionError):
        local_min = default_min
        local_max = default_max
    return local_min, local_max


def set_num(local_min, local_max, ui=True):
    if ui:
        print('\n# # Make sure that {} isn\'t looking!\n'.format(p2_name))
        local_num = input('Pick a number between {} and {} : '
                          .format(local_min, local_max))
    else:
        local_num = None
    try:
        local_num = int(local_num)
        assert local_min <= local_num <= local_max
    except (ValueError, AssertionError, TypeError):
        local_num = random.randint(local_min, local_max)
        if ui:
            print('You done messed up, A-A-Ron!')
            print('\nYour new number is {}\n'.format(local_num))
            input('Press ENTER to continue...')
    finally:
        clear()
    return local_num


def guess_num(local_min, local_max, p1_num, max_tries, tries=0, ui=True):
    tries = tries + 1
    print('\n# # Hint: Pick a number '
          'between {} and {}.'.format(local_min, local_max))
    if ui:
        p2_num = input('[{}/{}] Guess a number: '.format(tries, max_tries))
        try:
            p2_num = int(p2_num)
        except ValueError:
            p2_num = int(0)
    else:
        print('[{}/{}] Guess a number: '.format(tries, max_tries), end='')
        time.sleep(2)
        p2_num = random.randint(local_min, local_max)
        print(p2_num)
    if p2_num == p1_num:
        clear()
        print('Correctly guessed "{}" in {} tries!'.format(p1_num, tries))
        return p2_name
    elif p2_num > p1_num:
        print('Nope! {} is too high. Guess a lower number!'.format(p2_num))
        local_max = min((p2_num - 1), local_max)
    elif p2_num < p1_num:
        print('Nope! {} is too low. Guess a higher number!'.format(p2_num))
        local_min = max((p2_num + 1), local_min)
    if tries >= max_tries:
        clear()
        print('Too bad! The number was: {}'.format(p1_num))
        return p1_name
    winner = guess_num(local_min, local_max, p1_num, max_tries, tries, ui)
    return winner


def set_players(players=1):
    global p1_name, p2_name
    while p1_name == p2_name:
        p1_name = random.choice(p_names)
        p2_name = random.choice(p_names)
    if players == 0:
        p1_ui = p2_ui = False
    elif players == 2:
        p1_ui = p2_ui = True
    else:
        print(' 1 - Set the range and number to guess')
        print(' 2 - Guess the number, given a range')
        try:
            player_id = int(input('Please select a player: [2] ') or 2)
        except ValueError:
            player_id = 2
        p1_ui = True if player_id == 1 else False
        p2_ui = not p1_ui
    if p1_ui:
        p1_name = os.getlogin() if players == 1 else p1_name
        p1_name = input('Please enter a name for Player 1 [{}] '
                        .format(p1_name)) or p1_name
    if p2_ui:
        p2_name = os.getlogin() if players == 1 else p2_name
        p2_name = input('Please enter a name for Player 2 [{}] '
                        .format(p2_name)) or p2_name
    return p1_ui, p2_ui


if __name__ == '__main__':
    main()
