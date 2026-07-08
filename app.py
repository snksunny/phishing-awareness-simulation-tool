from flask import Flask #imports Flask class
from datetime import datetime #imports datetime class

app = Flask(__name__) #sets this as the main file of the project

@app.route("/landing/<tracking_id>") #sets the route for the landing page, captures the ID in <>
def landing_page(tracking_id): #defines the function for the landing page, passes the given parameter in () to the function
    now = datetime.now() #gets the current date and time
    with open("clicks_log.csv", "a") as file: #opens a CSV file in append mode, creates it if it doesn't exist
        file.write(f"{tracking_id},{now}\n") #writes the tracking ID and current date and time to a CSV file
    return f"Welcome to the landing page! Tracking ID: {tracking_id}" #returns a welcome message with the tracking ID, f is formating

if __name__ == "__main__": #checks if the file is being run directly and not imported into another file
    app.run(debug=True) #runs the app in debug mode