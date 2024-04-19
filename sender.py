from smtplib import SMTP
from email.mime.text import MIMEText

def sendMail(s_email,password,r_email,subject,body):
    msg=MIMEText(body)  # creating MIME object
    msg['From']=s_email
    msg['To']=r_email
    msg['Subject']=subject
    server=SMTP('smtp.gmail.com',587)  #define the gmail outgoing mail server name and port number
    server.starttls()  #Put the SMTP connection in TLS (Transport Layer Security) mode. All SMTP commands that follow will be encrypted
    server.login(s_email,password)  #logging in to the SMTP server
    server.sendmail(s_email,[r_email],msg.as_string())  #sending the message
    server.quit()  #Terminate the SMTP session and close the connection.

fromaddr="example@gmail.com"  #sender email
password="************"       #sender password
toaddr="example@gmail.com"  #reciever email
subject="Hello!!!!"  # subject of the mail
text="how are you?????"  # body of the mail
sendMail(fromaddr,password,toaddr,subject,text)
