import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

smtp_username = os.getenv("SMTP_USERNAME") 
smtp_password = os.getenv("SMTP_PASSWORD")

with open("email_template.html", "r") as file:
    email_template = file.read()

with open("targets.csv", "r") as file:
    reader = csv.DictReader(file)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(smtp_username, smtp_password)

    try: 
        for row in reader:
            name = row["name"]
            email = row["email"]
            tracking_id = row["tracking_id"] 

            tracking_link = f"http://127.0.0.1:5000/landing/{tracking_id}" 

            personalized_email = email_template.replace("{{name}}", name).replace("{{tracking_link}}", tracking_link)

            msg = MIMEMultipart()
            msg['From'] = smtp_username 
            msg['To'] = email
            msg['Subject'] = "Personalized Email"

            msg.attach(MIMEText(personalized_email, 'html'))

            server.send_message(msg)
            print(f"Email sent to {email}") 
    finally:
        server.quit() 
