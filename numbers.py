"""Le Compte Est Bon"""

import random

from utils import play_bell, start_timer

AVAILABLE_NUMBERS = [i for i in range(1, 11)] * 2 + [25, 50, 75, 100]
OPERATIONS = {
    "+": lambda x, y: x + y if x >= y else None,
    "-": lambda x, y: x - y if x > y else None,
    "x": lambda x, y: x * y if x <= y else None,
    "/": lambda x, y: x // y if y != 0 and x % y == 0 else None,
}


def draw_numbers():
    """
    Draws a random set of 6 numbers and a target number.

    Returns:
        tuple: A tuple containing a list of 6 sorted random numbers and the target number.
    """
    chiffres = random.sample(AVAILABLE_NUMBERS, 6)
    chiffres.sort()
    target = random.randint(100, 1000)
    return chiffres, target


def le_compte_est_bon(timer=45, extra_time=0):
    """
    Main game function to setup and start Le Compte Est Bon game.

    Args:
        timer (int): Time limit for the player to solve the game, in seconds.
        extra_time (int): Extra time added to the main timer for some players.

    Returns:
        tuple: A tuple containing the list of numbers drawn and the target number.
    """
    print("\n--- LE COMPTE EST BON ---")
    play_bell(wait=2)
    chiffres, target = draw_numbers()
    print(f"Cible: {target}")
    print(f"Chiffres: {' - '.join([str(c) for c in chiffres])}\n")
    start_timer(timer, extra_time)
