#Python program to read a text file into a list
#opening a file in read mode using open()
file = open('daftarEmail.txt', 'r')

#read text file into list
data = file.read().split(",")
#printing the data of the file
for d in data:
    print(d)