"""System that sends notifications by email"""

import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

print("db_user:", os.getenv("db_user"))
print("db_password:", os.getenv("db_password"))

#load environment variables from the .env file
load_dotenv()

#Retrieve environment variables securely
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT")
smtp_login = os.getenv("SMTP_LOGIN")
smtp_password = os.getenv("SMTP_PASSWORD")

sender_email = "test2@mail.com"
receiver_email = "test1@mail.com"
subject = "SWEET POTATOES CROP"

#Add plain text
text = """ Time to harvest the sweet potatoes is here! """

#create MIMEtext object 
message = MIMEText(text, "plain")
message["Subject"] = "Plain text email"
message["From"] = sender_email
message["To"] = receiver_email

#Send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls() #secure the connection
    server.login(smtp_login,smtp_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    
print("message sent successfully!")
