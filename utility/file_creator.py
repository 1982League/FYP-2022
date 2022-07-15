#!/usr/bin/python3
import time
from datetime import datetime

def fileWithDate(filename):
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    newFile = f'{filename}_{day}_{month}_{year}_{hour}_{minute}.txt'

    with open(filename, 'w') as f:
        f.write(newFile)
    return newFile


def fileWriter(filename):
    with open(filename) as f:
        f.write()
        f.write("\n")