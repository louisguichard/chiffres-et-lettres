from chiffres import le_compte_est_bon
from lettres import le_mot_le_plus_long

MENU = {
    "message": "A quoi voulez-vous jouer ?\n[1] Chiffres\n[2] Lettres\n",
    "actions": {"1": "chiffres", "2": "lettres"},
}


def get_user_choice():
    """
    Function to display menu and get user action.

    Returns:
        str: User selected action from the menu.
    """
    try:
        return MENU["actions"].get(input(MENU["message"]))
    except KeyboardInterrupt:
        quit


def main():
    """
    Main function to handle the game flow based on user input.
    """
    action = get_user_choice("start")
    while action:
        if action == "chiffres":
            try:
                le_compte_est_bon(timer=45, extra_timer=30)
            except KeyboardInterrupt:
                pass
            action = get_user_choice("numbers")
        elif action == "lettres":
            try:
                le_mot_le_plus_long(timer=30, extra_timer=0)
            except KeyboardInterrupt:
                pass
            action = get_user_choice("letters")


if __name__ == "__main__":
    main()
