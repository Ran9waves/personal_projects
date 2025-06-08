
import argparse #handles command line arguments

import plant_database


def main():
    parser = argparse.ArgumentParser(description="Automated Garden CLI")
    parser.add_argument(
        "--plant-db",
        action="store_true",
        help="Initializes plant_database.py and prints the actual db contents"
    )

    args = parser.parse_args()


    if args.plant_db:
        import plant_database

#ensures  that main() runs only when you execute * main.py directly (not when imported as a module)
if __name__ == "__main__":
    main()


