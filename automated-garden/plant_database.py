"""Manages (updates, adds, deletes elements) the database of the plants that I have planted in my garden.
It will be connected to notification_system.py to inform me when determinated events take place"""

##TO DO
# Create a database with the following information: plants that I have, when they were planted, when should
# I harvest them, issues that I had with them, where are they planted, quantity of light they need, watering period,
# add elements in my database
# delete elements in my database
# update elements in my database
# connect harvest data to cronjob and notification_system

import mysql.connector
import os

plantsdb = mysql.connector.connect(
    host="localhost",
    user=os.getenv("SMTP_LOGIN"),
    password= os.getenv("SMTP_PASSWORD"),
)

mycursor = plantsdb.cursor()
mycursor.execute("CREATE DATABASE plantsdatabase")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)