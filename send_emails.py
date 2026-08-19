import csv #imports the csv module for reading and writing CSV files
from email.mime.text import MIMEText #imports the MIMEText class for creating email messages
from email.mime.multipart import MIMEMultipart #imports the MIMEMultipart class for creating multipart email messages
import smtplib #imports the smtplib module for sending emails using the Simple Mail Transfer Protocol (SMTP)
import os #imports the os module for interacting with the operating system
from dotenv import load_dotenv #imports the load_dotenv function from the dotenv module for loading environment variables from a .env file

load_dotenv() #loads the environment variables from the .env file

smtp_username = os.getenv("SMTP_USERNAME") #gets the SMTP username from the environment variables
smtp_password = os.getenv("SMTP_PASSWORD") #gets the SMTP password from the environment variables

with open("email_template.html", "r") as file: #opens the email template file in read mode
    email_template = file.read() #reads the content of the email template file and stores it in a variable


with open("targets.csv", "r") as file:
    reader = csv.DictReader(file) #creates a DictReader object to read the CSV file as a dictionary
    server = smtplib.SMTP("smtp.gmail.com", 587) #creates an SMTP object for connecting to the Gmail SMTP server
    server.starttls() #starts TLS encryption for the SMTP connection
    server.login(smtp_username, smtp_password) #logs in to the SMTP server using the

    try: #precaution if anything fails mid loop
        for row in reader: #iterates through each row in the CSV file
            name = row["name"] #gets the name from the current row
            email = row["email"] #gets the email from the current row
            tracking_id = row["tracking_id"] #gets the tracking ID from the current row

            tracking_link = f"http://127.0.0.1:5000/landing/{tracking_id}" #creates a tracking link using the tracking ID

            personalized_email = email_template.replace("{{name}}", name).replace("{{tracking_link}}", tracking_link) #replaces the placeholders in the email template with the actual name and tracking link

            msg = MIMEMultipart() #creates a multipart email message
            msg['From'] = smtp_username #sets the sender's email address
            msg['To'] = email #sets the recipient's email address
            msg['Subject'] = "Personalized Email" #sets the subject of the email

            msg.attach(MIMEText(personalized_email, 'html')) #attaches the personalized email as an HTML message

            server.send_message(msg) #sends the email message
            print(f"Email sent to {email}") #prints a message indicating that the email was sent
    finally:
        server.quit() #closes the connection to the SMTP server
