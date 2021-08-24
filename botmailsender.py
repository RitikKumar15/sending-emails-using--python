import smtplib, ssl, getpass

port = 465  # For SSL
sender_email = "sendermail@gmail.com"
receiver_email  = "receivermail@gmail.com"
message = """\
Subject: Hi there

This message is sent from Python."""
password = getpass.getpass(prompt='Type your password and press enter: ')

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    # Send email here
    server.sendmail(sender_email, receiver_email, message)