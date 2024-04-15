import argparse
import yaml

from chiffres import le_compte_est_bon, solve_lceb
from lettres import le_mot_le_plus_long, solve_lmlpl


def load_config(profile="default"):
    """
    Load configuration settings from the YAML config file.

    Args:
        profile (str): Configuration profile name.

    Returns:
        dict: Dictionary containing profile-specific configurations.
    """
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)
    return config.get(profile)


MENUS = {
    "start": {
        "message": "Par quoi voulez-vous commencer ?\n[1] Chiffres\n[2] Lettres\n> ",
        "actions": {"1": "chiffres", "2": "lettres"},
    },
    "numbers": {
        "message": "[1] Voir la meilleure solution\n[2] Recommencer les chiffres\n[3] Passer aux lettres\n> ",
        "actions": {"1": "solution", "2": "chiffres", "3": "lettres"},
    },
    "numbers_sol": {
        "message": "[1] Recommencer les chiffres\n[2] Passer aux lettres\n> ",
        "actions": {"1": "chiffres", "2": "lettres"},
    },
    "letters": {
        "message": "[1] Voir la meilleure solution\n[2] Passer aux chiffres\n[3] Recommencer les lettres\n> ",
        "actions": {"1": "solution", "2": "chiffres", "3": "lettres"},
    },
    "letters_sol": {
        "message": "[1] Passer aux chiffres\n[2] Recommencer les lettres\n> ",
        "actions": {"1": "chiffres", "2": "lettres"},
    },
}


def get_user_choice(menu):
    """
    Function to display menu and get user action.

    Args:
        menu (str): Key for the menu dictionary.

    Returns:
        str: User selected action from the menu.
    """
    try:
        return MENUS[menu]["actions"].get(input(MENUS[menu]["message"]))
    except KeyboardInterrupt:
        quit


def main():
    """
    Main function to handle the game flow based on user input.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--profile",
        type=str,
        default="default",
    )
    args = parser.parse_args()
    config = load_config(args.profile)
    action = get_user_choice("start")
    while action:
        if action == "chiffres":
            try:
                numbers, target = le_compte_est_bon(
                    timer=config["numbers"]["timer"],
                    extra_timer=config["numbers"]["extra_timer"],
                )
            except KeyboardInterrupt:
                pass
            action = get_user_choice("numbers")
            if action == "solution":
                print("\n" + solve_lceb(numbers, target) + "\n")
                action = get_user_choice("numbers_sol")
        elif action == "lettres":
            try:
                letters = le_mot_le_plus_long(
                    timer=config["letters"]["timer"],
                    extra_timer=config["letters"]["extra_timer"],
                )
            except KeyboardInterrupt:
                pass
            action = get_user_choice("letters")
            if action == "solution":
                print("\n" + solve_lmlpl(letters) + "\n")
                action = get_user_choice("letters_sol")


if __name__ == "__main__":
    main()
