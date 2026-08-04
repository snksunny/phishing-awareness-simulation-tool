from flask import Flask #imports Flask class
from datetime import datetime #imports datetime class

app = Flask(__name__) #sets this as the main file of the project

@app.route("/landing/<tracking_id>") #sets the route for the landing page, captures the ID in <>
def landing_page(tracking_id): #defines the function for the landing page, passes the given parameter in () to the function
    now = datetime.now() #gets the current date and time
    with open("clicks_log.csv", "a") as file: #opens a CSV file in append mode, creates it if it doesn't exist
        file.write(f"{tracking_id},{now}\n") #writes the tracking ID and current date and time to a CSV file
    return f"""
    <html>
        <body>
            <h1>This was a phishing simulation</h1>
            <p>You clicked a link in a simulated phishing email, sent as part of a security awareness exercise.</p>
            <p>Here's what you should have noticed:</p>
            <ul>
                <li>Urgent, fear-based language ("act immediately")</li>
                <li>A generic greeting instead of specific details</li>
                <li>A suspicious or unfamiliar link destination</li>
            </ul>
            <p>Your tracking ID for this test: {tracking_id}</p>
        </body>
    </html>
    """

if __name__ == "__main__": #checks if the file is being run directly and not imported into another file
    app.run(debug=True) #runs the app in debug mode