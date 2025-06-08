"""Manages (updates, adds, deletes elements) the database of the plants that I have planted in my garden.
It will be connected to notification_system.py to inform me when determinated events take place"""

##TO DO
# pending: I harvest them, issues that I had with them, where are they planted, quantity of light they need, watering period,
# add elements in my database
# delete elements in my database
# update elements in my database
# connect harvest data to cronjob and notification_system

import psycopg2
import os

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
cur.execute("DROP TABLE IF EXISTS mygarden;")

#creates a table in the database if it does not exist.
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
cur.execute("DELETE FROM mygarden;")


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

#commit the changes to the database
cur.executemany("""
    INSERT INTO mygarden (plantname, plantdate, harvestdate, plantfruit, plantissues, plantdeath, cropphase, plantnext)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""", plants)


#commit the changes to the database
conn.commit()

# Print all rows to verify
cur.execute("SELECT * FROM mygarden;")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()


