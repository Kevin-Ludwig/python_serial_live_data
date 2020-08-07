import serial
import datetime
import sys
import keyboard
import random

try:
    ser = serial.Serial(
    port='COM3',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
    timeout=1)
    print("Connected to COM3")
except serial.SerialException:
    print("Error while connecting to port COM 3")
    sys.exit(0)

# current time for calculating the time values for incoming data
start_time = datetime.datetime.now()

# create a random event between 0 and 5
eventNumber = random.randint(0, 5)
eventCounter = 0

while True:
    data = ser.readline()
    data_encode = data.decode('ascii').strip()

    # Timestamp in seconds for every single data value
    time_diff = (datetime.datetime.now() - start_time)
    execution_time = str(time_diff.total_seconds())

    if eventCounter == 10:
        eventNumber = random.randint(0, 5)
        eventCounter = 0

    # Write data into textfile
    with open('output.txt', 'a') as text_file:
        text_file.write(execution_time + " " + str(eventNumber) + " " + str(data_encode) + "\n")

    eventCounter = eventCounter + 1

    # Break the loop for exiting the program via keyhandling
    if keyboard.is_pressed('s'):
        break
