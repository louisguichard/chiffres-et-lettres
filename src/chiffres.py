"""Le Compte Est Bon"""

import random

AVAILABLE_NUMBERS = [i for i in range(1, 11)] * 2 + [25, 50, 75, 100]
OPERATIONS = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
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


def solve_lceb(numbers, target, best_result=None):
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if i != j:
                a, b = numbers[i], numbers[j]
                x_min, x_max = min(a, b), max(a, b)
                remaining = [numbers[k] for k in range(n) if k != i and k != j]
                for op in OPERATIONS:
                    result = OPERATIONS[op](x_max, x_min)
                    if result is not None:
                        expression = (
                            f"{x_min} {op} {x_max} = {result}"
                            if op == "×"
                            else f"{x_max} {op} {x_min} = {result}"
                        )
                        if result == target or len(remaining) == 0:
                            next_result, next_expr = result, []
                        else:
                            next_attempt = solve_lceb(
                                remaining + [result], target, best_result
                            )
                            next_result, next_expr = next_attempt

                        if best_result is None:
                            best_result = (next_result, [expression] + next_expr)
                        else:
                            improvement = abs(target - best_result[0]) - abs(
                                target - next_result
                            )
                            if improvement > 0 or (
                                improvement == 0
                                and len([expression] + next_expr) < len(best_result[1])
                            ):
                                best_result = (next_result, [expression] + next_expr)
    return best_result
