"""This script checks the harvest date of plants in the database and afterwards calls 
the notification system to send an email notification if the harvest date matches today's date."""

import psycopg2
import os
from dotenv import load_dotenv
from datetime import date
from notification_system import send_notification

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("db_host"),
    database="mygarden",
    user=os.getenv("db_user"),
    password=os.getenv("db_password"),
    port=os.getenv("db_port")
)
cur = conn.cursor()

today = date.today().isoformat() # Get today's date in ISO format
cur.execute("SELECT plantname, harvestdate FROM mygarden WHERE harvestdate = %s", (today,))
plants = cur.fetchall() # Fetch all matching plants

for plant in plants:
    plantname = plant[0]
    # Call the notification system to send an email
    send_notification(
        f"Time to harvest the {plantname} is here!", 
        f"Today ({today}) is the harvest date for {plantname}."
)
     
cur.close()
conn.close()

