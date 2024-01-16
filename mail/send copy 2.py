import sys
import requests
from datetime import datetime

from formatting2 import format_msg
from hitungwaktu import countdownTimer

from main3 import send_mail

def send(name, website=None, to_email=None, verbose=False):
    assert to_email != None
    if website != None:
        msg = format_msg(my_name=name, my_website=website)
    else:
        msg = format_msg(my_name=name)
    if verbose:
        print(name, website, to_email)
    # send the message
    try:
        send_mail(text=msg, to_emails=[to_email], html=msg)
        sent = True
    except:
        sent = False
    return sent

if __name__ == "__main__":
    print(sys.argv)
    name = "Unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    email = 'bungafadilasari@gmail.com'
    if len(sys.argv) > 2:
        email = sys.argv[2]
    if countdownTimer(00,5) == True:
        response = send(name, to_email=email, verbose=True)
        print(response)
    else:
        print('waktu habis')