"""Le Mot Le Plus Long"""

import json
import random

from utils import play_bell, start_timer

with open("dictionnaire.json") as file:
    dictionary = json.load(file)

VOYELLES = "AEIOUY"
CONSONNES = "BCDFGHJKLMNPQRSTVWXZ"


def draw_letters():
    """
    Draw a balanced set of vowels and consonants.

    Returns:
        list: List of randomly chosen letters (5 vowels and 5 consonants).
    """
    letters = random.choices(VOYELLES, k=5) + random.choices(CONSONNES, k=5)
    random.shuffle(letters)
    return letters


def le_mot_le_plus_long(timer=30, extra_timer=0):
    """
    Main game function to setup and start 'Le Mot Le Plus Long' game.

    Args:
        timer (int): Main timer duration in seconds.
        extra_timer (int): Additional timer duration for some players.

    Returns:
        list: List of drawn letters for the game.
    """
    print("\n--- LE MOT LE PLUS LONG ---")
    play_bell(wait=2)
    letters = draw_letters()
    print(f"Lettres : {' - '.join(letters)}\n")
    start_timer(timer, extra_timer)
