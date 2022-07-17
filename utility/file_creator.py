#!/usr/bin/python3
import os
from datetime import datetime

def fileWithDate(filename):

    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    path= r'C:\Users\sjoshi\Desktop\code\FYP-2022\acl_rules\acl_'
    filename = f'{path}{filename}_{day}_{month}_{year}_{hour}_{minute}.txt'

    with open(os.path.join(path, filename),'w') as f:
        f.write("File Created!?")
        return f

def fileWriter(filename, filecontent):
    with open(filename,'w') as f:
        f.write(filecontent + "\n")
        return f

def main():
    fileWithDate('test')
    f=r'C:\Users\sjoshi\Desktop\code\FYP-2022\acl_rules\acl_test_17_7_2022_14_0.txt'
    fileWriter(f,"Write ACL here")
if __name__ == "__main__":
    main()
    exit()
