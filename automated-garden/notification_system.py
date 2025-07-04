"""System that sends notifications by email"""

import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

#load environment variables from the .env file
load_dotenv()

#Retrieve environment variables securely
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT")
smtp_login = os.getenv("SMTP_LOGIN")
smtp_password = os.getenv("SMTP_LOGIN_PASSWORD")

sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")
subject = "SWEET POTATOES CROP"

def send_notification(subject, text):
    """Function to send an email notification."""
    # Create a MIMEText object
    message = MIMEText(text, "plain")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure the connection
        server.login(smtp_login, smtp_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    
    print("Message sent successfully!")
