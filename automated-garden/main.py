from art import *
from simple_term_menu import TerminalMenu #for creating a terminal menu
import sys
import plant_database

print(text2art("""Automated Garden Project""",font="small")) # Prints the title in ASCII art

def main():
    # Create a command-line interface for the Automated Garden
    # This will allow users to initialize the database, add, update, or delete plants
    # and view the plant database contents.
    # This is the main entry point for the CLI application.

    options = {
        "Initialize Database": plant_database.initialize_database, # Initializes the plant database with default values
        "View Plant Database": plant_database.show_all_plants, # Displays all plants in the database
        "Add Plant": plant_database.add_plant, # Adds a new plant to the database
        "Update Plant": plant_database.update_plant_info, # Updates plant information in the database
        "Delete Plant": plant_database.delete_plant, # Deletes a plant from the database
        "Quit": sys.exit # Exits the application
    } # Defines the options for the menu

    menu_entries = list(options.keys()) # Gets the keys from the options dictionary
    terminal_menu = TerminalMenu(menu_entries) # Creates a terminal menu with the entries

    while True:
        choice_index = terminal_menu.show() # Displays the menu and gets the user's choice
        if choice_index is None:
            print("No available option selected, exiting.")
            break
        choice = menu_entries[choice_index]
        if choice == "Quit":
            print("Goodbye!")
            break
        options[choice]() # Calls the function associated with the selected option

if __name__ == "__main__":
    main() # Ensures that main() runs only when you execute main.py directly (not when imported as a module)


