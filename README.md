# Email Interaction Scripts
# Overview
This repository contains two Python scripts designed to interact with email services, particularly Gmail, using the IMAP and SMTP protocols. One script is for sending emails (sendMail() function), while the other is for retrieving and displaying details of the most recent email in the inbox.

# Script 1: Sender.py
Functionality:<br>
The sendMail() function sends an email message using Gmail's SMTP server. It accepts the sender's email address, password, recipient's email address, subject, and body text as input parameters. The function constructs an email message using the MIMEText module, sets the necessary headers (From, To, Subject), establishes a secure connection to the SMTP server (smtp.gmail.com:587), logs in using the sender's credentials, sends the email message, and then closes the connection.

Usage:<br>
To use the sendMail() function, simply call it with the required parameters:
```python
from sender.py import sendMail

fromaddr = "sender@gmail.com"
password = "your_password"
toaddr = "recipient@example.com"
subject = "Subject of the email"
text = "Body of the email"
sendMail(fromaddr, password, toaddr, subject, text)
```
# Script 2: Retrieve and Display Email Details
Functionality:<br>
This script retrieves the most recent email from the Gmail inbox using the IMAP protocol (IMAP4_SSL), parses the email message using the email module, and then displays the sender, subject, and content of the email. It establishes a secure connection to the Gmail IMAP server (imap.gmail.com:993), logs in using the user's credentials, selects the inbox mailbox, fetches the most recent email message, parses the message into its components (sender, subject, content), and then prints out these details.

Usage:<br>
To use the email retrieval script, run the Python script in your preferred environment:
```python
python reciever.py
```
# Dependencies
Both scripts require the following dependencies:

Python 3.x
imaplib module (for retrieving emails via IMAP)<br>
smtplib module (for sending emails via SMTP)<br>
email module (for parsing email messages)<br>
Ensure that you have these dependencies installed before using the scripts.


