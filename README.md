# phishing-awareness-simulation-tool

This is a tool that sends mock phishing emails to a list of recipients and tracks
whether they click the link, to help improve security awareness.
Intended for running and testing LOCALLY;

## Features

- Sends personalized mock phishing emails via Gmail SMTP
- Flask-based landing page that logs clicks with a timestamp (locally)
- Page after clicking, explaining what to watch out for
- Reporting script that summarises click rate of all targets

## Setup

1. Clone the repo
2. Create and activate a virtual environment
3. Install dependencies: 'pip install -r requirements.txt'
4. Create a '.env' file with:
    - SMTP_USERNAME=your_email@ gmail.com 
    - SMTP_PASSWORD=your_app_password
5. Create a 'targets.csv' file with columns: 'name,email,tracking_id'

## Usage

1. Start the tracking server: 'python app.py'
2. In a separate terminal, send the emails: 'python send_emails.py'
3. Generate a report: 'python report.py'

