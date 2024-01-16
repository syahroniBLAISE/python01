import imaplib
import email

imap_server = "imap.gmail.com"
email_adress = "bungafadilasari@gmail.com"
password = 'jbmw jfmp pzvn biru'

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_adress, password)

imap.select('"[Gmail]/Sent Mail"')
# imap.select('Inbox')

_, msgnums = imap.search(None, "ALL")

for msgnum in msgnums[0].split():
    _, data = imap.fetch(msgnum, "(RFC822)")
    message = email.message_from_bytes(data[0][1])

    # print(f"subject : {message.get('Subject')}")
    print(f"to : {message.get('To')}")

    for part in message.walk():
        if part.get_content_type() == "text/plain":
            # print(part.as_string())
            ()
imap.close()