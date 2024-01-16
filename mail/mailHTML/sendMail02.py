
# server = smtplib.SMTP('smtp.gmail.com', 587)

# # Make sure to give app access in your Google account
# server.login('bungafadilasari@gmail.com', 'jbmw jfmp pzvn biru')

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# environment variables
username = 'bungafadilasari@gmail.com'
password = 'jbmw jfmp pzvn biru'

def send_mail(text='Email Body', subject='Hello World', from_email='test <bungafadilasari@gmail.com>', to_emails=None, html=None):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject
    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)
    if html != None:
        html_part = MIMEText(html, 'html')
        msg.attach(html_part)
    msg_str = msg.as_string()
    # login to my smtp server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()
    # with smtplib.SMTP() as server:
    #     server.login()
    #     pass

# send_mail(html="<h1>Ini dari HTML part</h1>")
    # ['bungafadilasari@gmail.com']


