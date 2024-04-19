# Email Interaction Scripts
# Overview
This repository contains two Python scripts designed to interact with email services, particularly Gmail, using the IMAP and SMTP protocols. One script is for sending emails (sendMail() function), while the other is for retrieving and displaying details of the most recent email in the inbox.

Script 1: Sender.py
Functionality
The sendMail() function sends an email message using Gmail's SMTP server. It accepts the sender's email address, password, recipient's email address, subject, and body text as input parameters. The function constructs an email message using the MIMEText module, sets the necessary headers (From, To, Subject), establishes a secure connection to the SMTP server (smtp.gmail.com:587), logs in using the sender's credentials, sends the email message, and then closes the connection.

Usage
To use the sendMail() function, simply call it with the required parameters:
```python
from sendMail import sendMail

fromaddr = "sender@gmail.com"
password = "your_password"
toaddr = "recipient@example.com"
subject = "Subject of the email"
text = "Body of the email"
sendMail(fromaddr, password, toaddr, subject, text)
```
