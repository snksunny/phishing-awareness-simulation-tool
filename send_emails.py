import csv #imports the csv module for reading and writing CSV files

with open("email_template.html", "r") as file: #opens the email template file in read mode
    email_template = file.read() #reads the content of the email template file and stores it in a variable


with open("targets.csv", "r") as file:
    reader = csv.DictReader(file) #creates a DictReader object to read the CSV file as a dictionary
    for row in reader: #iterates through each row in the CSV file
        name = row["name"] #gets the name from the current row
        email = row["email"] #gets the email from the current row
        tracking_id = row["tracking_id"] #gets the tracking ID from the current row

        tracking_link = f"http://127.0.0.1:5000/landing/{tracking_id}" #creates a tracking link using the tracking ID

        personalized_email = email_template.replace("{{name}}", name).replace("{{tracking_link}}", tracking_link) #replaces the placeholders in the email template with the actual name and tracking link

        print(personalized_email) #prints the personalized email to the console