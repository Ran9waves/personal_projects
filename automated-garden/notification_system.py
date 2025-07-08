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

if smtp_port and smtp_port.strip():
    smtp_port = int(smtp_port)
else:
    smtp_port = 587

def send_notification(subject, text):
    """Function to send an email notification."""
    # Create a MIMEText object
    message = MIMEText(text, "plain")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    try:
        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()
            server.starttls()  # Secure the connection
            server.ehlo()
            server.login(smtp_login, smtp_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")
        raise
    else:
        print("Message sent successfully!")
