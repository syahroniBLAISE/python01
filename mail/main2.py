import smtplib
from email.message import EmailMessage

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
# Make sure to give app access in your Google account
server.login('bungafadilasari@gmail.com', 'jbmw jfmp pzvn biru')
email = EmailMessage()
email['From'] = 'bungafadilasari@gmail.com'
email['To'] = 'bungafadilasari@gmail.com'
email['Subject'] = 'test'
email.set_content('test')
server.send_message(email)