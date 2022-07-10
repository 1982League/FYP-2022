#!/usr/bin/python3
import time
import serial


def open_console(port='com8', baudrate=9600):
    """This method will create serial connection to the given network device
    port may need to be changed as per hardware.
    """
    console = serial.Serial(port='com8', baudrate=9600, parity='N', stopbits=1, bytesize=8, timeout=8)
    if console.isOpen():
        return console
    else:
        return False

def run_command(console, cmd='\n', sleep=2):
    """This method sends commands via serial connection, slower."""
    print('Sending command ' + cmd)
    console.write(cmd.encode() + b'\n')
    time.sleep(sleep)

def check_intial_config(console):
    """This method deals with initial configuration dialog in devices."""
    run_command(console,'\n')
    prompt = read_from_console(console)
    if 'Would you like to enter initial configuration dialog?' in prompt:
        run_command(console, 'no\n', 15)
        run_command(console, '\r\n')

def read_from_console(console):
    """This function Reads output from the console"""
    bytes_to_be_read = console.inWaiting()
    if bytes_to_be_read:
        output = console.read(bytes_to_be_read)
        return output.decode()
    else:
        return False

# Testing commands
con = open_console()
run_command(con)
run_command(con, 'enable', 2)
run_command(con, 'netlab', 2)
run_command(con)
run_command(con, 'show ip int br', 5)
output = read_from_console(con)
print(output)
