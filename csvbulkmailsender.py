import csv, smtplib, ssl, getpass

port = 465  # For SSL
sender_email = "sendermail@gmail.com"
password = getpass.getpass(prompt='Type your password and press enter: ')
message = """
Subject: Hi {name}

Your assignment grade is {grade}."""

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    # opening the csv file
    with open("list.csv") as file:
        reader = csv.reader(file)
        #next(reader) # Skip header row
        for name, email, grade in reader:
            server.sendmail(
                sender_email,
                email,
                message.format(name=name, grade=grade)
            )
            
        