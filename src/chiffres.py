"""Le Compte Est Bon"""

import random
import itertools

AVAILABLE_NUMBERS = [i for i in range(1, 11)] * 2 + [25, 50, 75, 100]
OPERATIONS = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y if x > y else None,
    "×": lambda x, y: x * y,
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

    # Explore all combinations of numbers and operations
    for num_count in range(2, len(numbers) + 1):  # count of numbers used
        for combination in itertools.permutations(
            numbers, num_count
        ):  # all possible combinations
            for ops in itertools.product(
                OPERATIONS, repeat=len(combination) - 1
            ):  # all possible operations
                result, steps = evaluate_expression(combination, ops)
                if result is None:  # skip invalid operations
                    continue
                if result == target:  # return exact solution
                    return steps
                diff = abs(target - result)
                if diff < best_diff:
                    best_diff = diff
                    best_solution = steps
    return best_solution
