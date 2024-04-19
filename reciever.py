from imaplib import IMAP4_SSL
import email

username="example@gmail.com"
password="***********"
server=IMAP4_SSL('imap.gmail.com')  # gmail incoming mail server
server.login(username,password)
res,msgnums=server.select()  # default mailbox:inbox
if res == 'OK':
    # Fetch the most recent message in the mailbox
    res, data = server.fetch(msgnums[0], "(RFC822)")
    if res == 'OK':
        for response_part in data:
           if isinstance(response_part, tuple):
                message = email.message_from_bytes(response_part[1])
                # getting message details
                mail_from = message['from']
                mail_subject = message['subject']
                mail_content = message.get_payload(decode=True)
                # printing message details
                print(f'From: {mail_from}')
                print(f'Subject: {mail_subject}')
                print(f'Content: {mail_content}')
    else :
        print("error fetching message:",res)
else:
    print("error selecting mailbox:",res)
