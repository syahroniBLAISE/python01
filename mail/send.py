import sys
import requests
import pandas as pd

# importing xlwt module 
import xlwt 

# Regex
import re

from datetime import datetime
from random import randint # untuk bilangan random

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
        # send_mail(text=msg, to_emails=[to_email], html=msg)

        sent = True
    except:
        sent = False
    return sent

if __name__ == "__main__":
    print(sys.argv)
    name = "Unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    emails = list
    if len(sys.argv) > 2:
        email = sys.argv[2]
    # mengenerate 5 bil bulat 0 s/d 10
    
    #Python program to read a text file into a list
    #opening a file in read mode using open()
    # file = open('daftarEmail.txt', 'r')
    # data = file.read().split(",")
    
    
    # openCSV
    file = pd.read_excel('test.xlsx')
    # print(type(file))
    # print(file)
    data = file['email'].values
    # print(email)

    #read text file into list
   
    #printing the data of the file
    workbook = xlwt.Workbook()  
  
    sheet = workbook.add_sheet("Email Target") 
    
    # Regex email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    # Applying multiple styles 
    
    
    row = 1
    response = ''
    for email in data:
        for i in range(5):
            timeRange = randint(2, 3)
            if countdownTimer(00,timeRange) == True:
                # pass the regular expression
                # and the string into the fullmatch() method
                # print(email)
                if(re.fullmatch(regex, email)):
                    print(email + " = Valid Email")
                    response = send(name, to_email=email, verbose=True)
                    print('response ='+ str(response))
                    style = xlwt.easyxf('font: bold 1, color green;') 
                else:
                    print(email + " = Invalid Email")
                    response = 'invalid'
                    style = xlwt.easyxf('font: bold 1, color red;') 
                
                print('rentang waktu = '+ str(timeRange))
                print('ini baris'+ str(row))
                sheet.write(row, 1, email)
                sheet.write(row, 2, response, style)
                workbook.save("sample.xls") 
                print('x---------------------------------------------------------x')
                row =row+1
                break
            else:
                print('waktu Gagal')





    
    # Writing on specified sheet 
    # sheet.write(0, 0, 'SAMPLE', style) 
    # sheet.write(2, 0, '1', style) 
    # sheet.write(0, 2, '2', style) 
    
    