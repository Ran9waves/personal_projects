"""Manages (updates, adds, deletes elements) the database of the plants that I have planted in my garden.
It will be connected to notification_system.py to inform me when determinated events take place"""

##TO DO
# Create a database with the following information: plants that I have, when they were planted, when should
# I harvest them, issues that I had with them, where are they planted, quantity of light they need, watering period,
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

#creates a table in the database if it does not exist.
#column values of the database: id, plant_name, planted_date, harvest_date
cur.execute("""
            CREATE TABLE mygarden (
            id SERIAL PRIMARY KEY,
            plant_name VARCHAR(100),
            planted_date DATE,
            harvest_date DATE
        )
""")

#commit the changes to the database
cur.execute("""
    INSERT INTO mygarden (plant_name, planted_date, harvest_date) 
    VALUES 
        ('Purple sweet potato', '2025-05-14', '2025-08-14')
""")

#commit the changes to the database
conn.commit()
#close the cursor and connection
cur.close()
conn.close()

