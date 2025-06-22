"""Manages (updates, adds, deletes elements) the database of the plants that I have planted in my garden.
It will be connected to notification_system.py to inform me when determinated events take place"""

##TO DO
# add elements in my database
# delete elements in my database
# connect harvest data to cronjob and notification_system

import psycopg2
import os
from dotenv import load_dotenv

#load environment variables from the .env file
load_dotenv()  # loads your .env file

#checks if the environment variables for database user and password are set
db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
if not db_user or not db_password:
    raise ValueError("Database user and password must be set in environment variables.")

#connects database with python
conn = psycopg2.connect(
    host= os.getenv("db_host"),
    database = "mygarden",
    user=db_user,
    password= db_password,
    port = os.getenv("db_port")
    )
    

# the cursor object will allow us to execute SQL commands on our database
cur = conn.cursor()

# In case there's an old outdated table, we drop it to start fresh.
#cur.execute("DROP TABLE IF EXISTS mygarden;")

#Only creates a table in the database if it does not exist.
#column values of the database: id, plant_name, planted_date, harvest_date
cur.execute("""
            CREATE TABLE IF NOT EXISTS mygarden (
            id SERIAL PRIMARY KEY,
            plantname VARCHAR(255),
            plantdate DATE NOT NULL,
            harvestdate DATE,
            plantfruit VARCHAR(255),
            plantissues VARCHAR(255),
            plantdeath DATE,
            cropphase VARCHAR(255),
            plantnext VARCHAR(255)
        )
""")

# Clear table for testing (optional, remove in production)
#cur.execute("DELETE FROM mygarden;")


# This is a list of tuples, where each tuple represents a row to be inserted into the database.
plants = [
    ('buddha hand lime','2025-05-04',None,None,'Red spider. Already cured',None,'Phase 4: Misc','Phase 1: Potatoes'),
    ('white finger lime','2025-04-15',None,None,'Mold. Still in treatment',None,'Phase 4: Misc','Phase 1: Potatoes'),
    ('strawberries','2025-04-12','2025-05-01','2','None',None,'Phase 4: Misc','Phase 1: Potatoes'),
    ('red finger lime','2025-04-05',None,None,'None',None,'Phase 4: Misc','Phase 1: Potatoes'),
    ('raspberries','2025-04-12','2025-04-26','3','None',None,'Phase 4: Misc','Phase 1: Potatoes'),
    ('mint','2024-04-26','2024-04-26','since it grew','None',None,'Phase 4: Misc','Phase 1: Potatoes'),
    ('purple sweet potato','2025-11-23',None,None,'Unidentified nibbing bug',None,'Phase 1: Potatoes','Phase 2: beans'),
    ('giant carrots','2025-05-15',None,None,'flood','2025-05-30','Phase 3: beets','Phase 1: Misc'),
    ('setubal onion','2025-05-04',None,None,'None',None,'Phase 3: beets','Phase 4: Misc'),
    ('cherry tomatoes','2025-04-12',None,None,'None',None,'Phase 4: Misc','Phase 1: Potatoes'),
    ('lettuce','2025-05-20',None,None,'None',None,'Phase 4: Misc','Phase 1: Potatoes'),
    ('kohlrabi','2025-05-20',None,None,'None',None,'Phase 3: beet','Phase 4: beets'),
    ('beet','2025-05-04',None,None,'None',None,'Phase 3: beets','Phase 4: misc'),
    ('melon ananas','2025-05-20',None,None,'None',None,'Phase 4: Misc','Phase 1: Potatoes'),
    ('radish','2025-04-12',None,None,'None',None,'Phase 3: Misc','Phase 4: misc'),
    ('watermelon','2025-04-05',None,None,'None',None,'Phase 1: Misc','Phase 4: Potatoes'),
    ('basilicum','2025-05-04','2025-05-04',None,'None',None,'Phase 4: Misc','Phase 1: Potatoes')
]

# Insert initial data only if the table is empty
cur.execute("SELECT COUNT(*) FROM mygarden;")
if cur.fetchone()[0] == 0:
    cur.executemany("""
        INSERT INTO mygarden (plantname, plantdate, harvestdate, plantfruit, plantissues, plantdeath, cropphase, plantnext)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, plants)
    conn.commit()

def initialize_database():
    """(Re)creates the mygarden table and inserts the default plants."""
    cur.execute("DROP TABLE IF EXISTS mygarden;")
    cur.execute("""
        CREATE TABLE mygarden (
            id SERIAL PRIMARY KEY,
            plantname VARCHAR(255),
            plantdate DATE NOT NULL,
            harvestdate DATE,
            plantfruit VARCHAR(255),
            plantissues VARCHAR(255),
            plantdeath DATE,
            cropphase VARCHAR(255),
            plantnext VARCHAR(255)
        )
    """)
    cur.executemany("""
        INSERT INTO mygarden (plantname, plantdate, harvestdate, plantfruit, plantissues, plantdeath, cropphase, plantnext)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, plants)
    conn.commit()
    print("Database initialized with default plants db.")

def show_all_plants():
    """prints all the plants in the database"""

    cur.execute("SELECT * FROM mygarden;")
    rows = cur.fetchall()
    print("\nCurrent plants in the database;")
    for row in rows:
        print(row)

def add_plant():
    """adds a new full entry ((whole plant information))"""
    print("\n ---Add a new plant to the database---")
    #requesting user input to create a new plant entry
    plantname = input("Enter the name of the plant: ")
    plantdate = input("Enter the planting date (YYYY-MM-DD): ")
    harvestdate = input("Enter the harvest date (YYYY-MM-DD, leave empty if not applicable): ")
    plantfruit = input("Enter how many times the plant provided fruit (leave empty if not applicable): ")
    plantissues = input("Enter any issues with the plant (leave empty if none): ")
    plantdeath = input("Enter the date of plant's death (YYYY-MM-DD, leave empty if not applicable): ")
    cropphase = input("Enter the current crop phase of the plant: ")
    plantnext = input("Enter the next plant to be planted after this one: ")

    #convert empty strings to None
    harvestdate = harvestdate if harvestdate else None
    plantfruit = plantfruit if plantfruit else None
    plantissues = plantissues if plantissues else None
    plantdeath = plantdeath if plantdeath else None

    cur.execute("""
        INSERT INTO mygarden (plantname, plantdate, harvestdate, plantfruit, plantissues, plantdeath, cropphase, plantnext)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (plantname, plantdate, harvestdate, plantfruit, plantissues, plantdeath, cropphase, plantnext))
    conn.commit()
    print("Plant added successfully!")
    show_all_plants() # Show all plants after adding a new one

def delete_plant():
    print("\n ---Delete a plant from the database")

    #prompts a list of all the plants in the database
    cur.execute("SELECT id, plantname FROM mygarden;")
    print("This is the current list of plants in the database:")
    for plant in cur.fetchall():
        print(f"ID: {plant[0]}, Name: {plant[1]}")

    #requests the user to input the ID of the plant they want to delete
    plant_id = input("Enter the ID of the plant you want to delete: ")
    cur.execute("DELETE FROM mygarden WHERE id = %s", (plant_id,))
    conn.commit()
    print("Plant deleted successfully!")
    show_all_plants() # Show all plants after adding a new one


def update_plant_info():
    print("\n ---Update plant information with your input---")
    plant_id = input("Enter the ID f the plant that you want to update: ")
    column = input("Which field do you want to update? (plantname, plantdate, harvestdate, plantfruit, plantissues, plantdeath, cropphase, plantnext): ")
    new_value = input(f"Enter the new value for {column} (leave empty for NULL): ")
    
    #Handle NULL values
    if new_value == "":
        new_value = None

    #Build and execute the update query
    query = f"UPDATE mygarden SET {column} = %s WHERE id = %s"
    cur.execute(query, (new_value, plant_id))
    conn.commit()
    print("Update successful!")
    show_all_plants() # Show all plants after adding a new one

# Insert data only if running as main and not updating
if __name__ == "__main__":
    update = input("\nDo you want to update plant information? (yes/no): ")
    if update.lower() == "yes":
        update_plant_info()
    else:
        cur.executemany("""
            INSERT INTO mygarden (plantname, plantdate, harvestdate, plantfruit, plantissues, plantdeath, cropphase, plantnext)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, plants)
        conn.commit()

    # Print all rows to verify
    cur.execute("SELECT * FROM mygarden;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
