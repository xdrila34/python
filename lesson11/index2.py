import datetime
import os.path
from os import linesep

currentdate = datetime.datetime.now()

print("year:", currentdate.year)
print("month:", currentdate.month)
print("day:", currentdate.day)
print("hour:", currentdate.hour)
print("minute:", currentdate.minute)
print("second:", currentdate.second)

current_date = datetime.datetime.now().date()

print(current_date)

set_time = datetime.datetime.now().time()

specifictime = datetime.date(2000, 2 , 2 , )

print(specifictime)

plusdays = currentdate + datetime.timedelta(days=100)
print(plusdays)
minusdays = currentdate - datetime.timedelta(days=100)
print(minusdays)

teksit =("this is the text i \n want to wirte")
with open("example.txt" , "w") as file:
    print(teksit)

file_path = ("example.txt","r")
file = open(file_path)

content = file.read()
print(content)
file.close()

with open("example.txt" , "r") as file:
    lines = file.readlines()
    print(lines)

with open("example.txt" , "r") as file:
    line = file.readline()
    print(line)

if os.path.exists("example.txt"):
    print(file)
