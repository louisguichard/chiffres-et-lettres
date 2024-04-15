"""Le Compte Est Bon"""

import random
import itertools

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
    return chiffres, target


def evaluate_expression(numbers, operations):
    """
    Evaluates the mathematical expression defined by numbers and operations.

    Args:
        numbers (list): The numbers used in the expression.
        operations (list): The operations applied between numbers.

    Returns:
        tuple: A tuple of the result of the expression and the list of steps showing the calculation.
    """
    value = numbers[0]
    steps = []
    for i, operation in enumerate(operations):
        next_number = numbers[i + 1]
        new_value = OPERATIONS[operation](value, next_number)
        if new_value is None:
            return None, None  # invalid operation
        steps.append(f"{value} {operation} {next_number} = {new_value}")
        value = new_value
    return value, steps


def solve_lceb(numbers, target):
    """
    Find the best sequence of operations that approximates or matches the target number.

    Args:
        numbers (list): List of numbers to use.
        target (int): Target number to reach.

    Returns:
        str: A string representing the best sequence that either matches or approximates the target.
    """
    best_diff = float("inf")
    best_solution = None

    # Explore all combinations of numbers and operations.
    for num_count in range(2, len(numbers) + 1):
        for combo in itertools.permutations(numbers, num_count):
            for ops in itertools.product(OPERATIONS, repeat=len(combo) - 1):
                result, steps = evaluate_expression(combo, ops)
                if result is None:  # skip invalid operations
                    continue
                if result == target:  # return exact solution
                    return "\n".join(steps)
                diff = abs(target - result)
                if diff < best_diff:
                    best_diff = diff
                    best_solution = steps

    return "\n".join(best_solution)
