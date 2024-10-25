"""Program code"""

# David Barnes, Robert Depweg
# CIS 226
# 6-4-2023

# First-party imports
import droids
from userinterface import UserInterface


def main(*args):
    """Method to run program"""

    # Create a new instance of droid collection
    droid_collection = droids.DroidCollection()

    # Create dummy data
    droid_collection.add_janitor(TEARS_OF_A_JEDI, WHITE, True, False, True, False, True)
    droid_collection.add_protocol(VANADIUM, RED, 6)
    droid_collection.add_astromech(QUADRANIUM, GREEN, True, False, True, False, 5)
    droid_collection.add_utility(CARBONITE, RED, True, False, True)
    droid_collection.add_utility(VANADIUM, BLUE, False, True, False)
    droid_collection.add_protocol(QUADRANIUM, BLUE, 3)
    droid_collection.add_janitor(CARBONITE, GREEN, False, True, True, False, True)
    droid_collection.add_astromech(TEARS_OF_A_JEDI, WHITE, False, True, False, False, 30)

    # Create a new instance of the user interface
    user_interface = UserInterface(droid_collection)

    # Display greeting to user
    user_interface.display_greeting()

    # Display main menu and get choice from user
    choice = user_interface.get_menu_choice(3, user_interface.display_main_menu)

    # While the choice is not 3 (exit)
    while choice < 3:
        # If 1, create droid
        if choice == 1:
            user_interface.create_droid()
        # Else if 2, print list
        elif choice == 2:
            list_choice = user_interface.get_print_choice(2, user_interface.display_list_options)
            # If 1, print list in stack format
            if list_choice == 1:
                droid_collection.category_sort()
            # If 2, print list in queue format
            elif list_choice == 2:
                droid_collection.category_sort()
            
        elif choice == 3:
            user_interface.sort_list()
        # Re-prompt for input
        choice = user_interface.get_menu_choice(3, user_interface.display_main_menu)

    # Display exiting program message.
    user_interface.display_exit_message()
