import smtplib, ssl, getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465  # For SSL
sender_email = "sendermail@gmail.com"
receiver_email  = "receivermail@gmail.com"
password = getpass.getpass(prompt='Type your password and press enter: ')

message = MIMEMultipart("alternative")

message["subject"] = "mutlipart testing"
message["From"] = "sendermail@gmail.com"
message["To"] = "receivermail@gmail.com"

# creating the plain text and html text versions

text = '''
Hi
How are you bro?
You know that that real python has many great tutorials:
www.realpython.com'''

html = '''
<html>
    <body>
        <p>Hi,<br />
            How are you bro!<br />
            <a href="www.realpython.com">Real python</a> has many great tutorials.
        </p>
    </body>
</html> 
'''

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    # Send email here
    server.sendmail(sender_email, receiver_email, message.as_string())