"""This script checks the harvest date of plants in the database and afterwards calls 
the notification system to send an email notification if the harvest date matches today's date."""

import os
from dotenv import load_dotenv
from datetime import date
from notification_system import send_notification

load_dotenv()

today = date.today().isoformat() # Get today's date in ISO format

with open('mygarden_export.csv'):
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row["harvestdate"] == today:
            plantname = row["plantname"]
            send.notification(
                f'Time to harvest {plantname} is ready to be harvested',
                f'Today is the day to harvest your {plantname}. Make sure to check your garden and collect the fruits or vegetables. Happy harvesting!'
            )
