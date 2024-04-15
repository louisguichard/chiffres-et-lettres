"""Le Mot Le Plus Long"""

import json
import random
from unidecode import unidecode

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
    return letters


def solve_lmlpl(letters):
    """
    Find the longest words from a set of letters.

    Args:
        letters (list): List of letters to form words.

    Returns:
        str: A formatted string showing the longest possible words.
    """
    letters_count = {letter: letters.count(letter) for letter in set(letters)}
    longest_words = [""]
    for raw_word in dictionary:
        word = unidecode(raw_word).upper()
        word_count = {letter: word.count(letter) for letter in set(word)}
        word_is_valid = all(
            word_count[letter] <= letters_count.get(letter, 0) for letter in word_count
        )
        if word_is_valid:
            if len(word) > len(longest_words[0]):
                longest_words = [word]
            elif len(word) == len(longest_words[0]):
                longest_words.append(word)
    longest_words = set(longest_words)
    if len(longest_words) <= 5:
        return f"En {len(longest_words[0])} lettres : {' / '.join(longest_words)}"
    return f"En {len(longest_words[0])} lettres : {' / '.join(longest_words[:5])} ..."
