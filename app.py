from flask import Flask
from datetime import datetime

app = Flask(__name__) 

@app.route("/landing/<tracking_id>") 
def landing_page(tracking_id): 
    now = datetime.now()
    with open("clicks_log.csv", "a") as file: 
        file.write(f"{tracking_id},{now}\n")
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

if __name__ == "__main__": 
    app.run(debug=True) 