import smtplib
from email.message import EmailMessage
email_subject = "Hello From Communcation Engineer"
sender_email_address = "networkprogramming0@gmail.com"
receiver_email_address = ["alaa9705549@gmail.com","sarashahla861@gmail.com"]
email_smtp = "smtp.gmail.com"
email_password = "bnvygusypogkbhne"

# create an email message object
message = EmailMessage()

# configure email headers
message['Subject'] = email_subject
message['From'] = sender_email_address
message['To'] = receiver_email_address

# set email body text
message.set_content("Hello, Our names is sara and farah and alaa")

# set smtp server and port
server = smtplib.SMTP(email_smtp, '587')
# identify this client to the SMTP server
print("gg")

server.ehlo()
# secure the SMTP connection
server.starttls()

# login to email account
server.login(sender_email_address, email_password)
# send email
server.send_message(message)
# close connection to server
server.quit()
