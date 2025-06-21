
import argparse #handles command line arguments
import sys

import plant_database


def main():
    parser = argparse.ArgumentParser(description="Automated Garden CLI")
    parser.add_argument(
        "--plant-db",
        action="store_true",
        help="Initializes plant_database.py and prints the actual db contents"
    )

    parser.add_argument(
        "--update-plant",
        action="store_true",
        help="Updates plant database through user input"
    )

    parser.add_argument(
        "--delete-plant",
        action="store_true",
        help="Deletes a plant from the database"
    )

    parser.add_argument(
        "--add-plant",
        action="store_true",
        help="Adds a new plant to the database"
    )

    args = parser.parse_args()

    if args.plant_db:
        import plant_database
    elif args.update_plant:
        plant_database.update_plant_info()
    elif args.delete_plant:
        plant_database.delete_plant()
    elif args.add_plant:
        plant_database.add_plant()
    else:
        print("No valid command provided. Use --plant-db to view the database or --update-plant to update it.")
        sys.exit(1)

    
#ensures  that main() runs only when you execute * main.py directly (not when imported as a module)
if __name__ == "__main__":
    main()


