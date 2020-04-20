# https://realpython.com/python-send-email/
#    python -m smtpd -c DebuggingServer -n localhost:1025
# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.message import EmailMessage

def send_alert(textfile):
    # Open the plain text file whose name is in textfile for reading.
    with open(textfile) as fp:
        # Create a text/plain message
        msg = EmailMessage()
        msg.set_content(fp.read())
    
    # me == the sender's email address
    # you == the recipient's email address
    me='ofg850@hotmail.com'
    you='ofg850@hotmail.com'
    msg['Subject'] = f'The contents of {textfile}'
    msg['From'] = me
    msg['To'] = you
    
    # Send the message via our own SMTP server.
    s = smtplib.SMTP('localhost:1025')
    s.send_message(msg)
    s.quit()

