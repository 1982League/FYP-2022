#!/usr/bin/python3
import os, sys, re
from datetime import datetime

class Utility:

    def __init__(self, filename):

        self.filename = filename

    def fileWithDate(self):

        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute
        second = now.second
        path= r'C:\Users\sjoshi\Desktop\code\FYP-2022\acl_rules\acl_'
        filename = f'{path}{self.filename}_{day}_{month}_{year}_{hour}_{minute}_{second}.txt'

        with open(os.path.join(path, filename),'w') as f:
            f.write("File Created!?")
            return f

    def fileWriter(filename, filecontent):
        with open(filename,'w') as f:
            f.write(filecontent + "\n")
            return f

    def findIpFromFile(self):
        f = open(sys.argv[1], 'r')
        # Enter the ip address you are searching for in the file
        ip = input("IP: ")
        # Reads the given parameter file
        text = f.read()
        # create empty list
        ips = []
        # regex to find pattern mattching to ip addresses
        regex = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text)

        # check if the regex is not none will never be
        if regex is not None:
            # looking for the match in the regex
            for match in regex:
                # if match is found in the list append it
                if match not in ips:
                    ips.append(match)
                    # Search the ip in the ip list from the file and display
                    if ip in match:
                        print(f"{ip} is in the file")
                        break
                else:
                    print(f"{ip} not found")
                    break
def main():

    fw = Utility('test')
    fw.fileWithDate()
    #f=r'C:\Users\sjoshi\Desktop\code\FYP-2022\acl_rules\acl_test_17_7_2022_14_0.txt'
    #fileWriter(f,"Write ACL here")
if __name__ == "__main__":
    main()
    exit()
