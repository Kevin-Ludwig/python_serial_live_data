import serial
import datetime
import sys
import keyboard

try:
    ser = serial.Serial(
    port='COM3',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
    timeout=1)
    print("Connected to COM 3")
except serial.SerialException:
    print("Error while connecting to port COM 3")
    sys.exit(0)

# current time for calculating the time values for incoming data
start_time = datetime.datetime.now()

while True:
    data = ser.readline()
    data_encode = data.decode('ascii').strip()

    # Timestamp in seconds for every single data value
    time_diff = (datetime.datetime.now() - start_time)
    execution_time = str(time_diff.total_seconds())

    # Write data into textfile
    with open('output.txt', 'a') as text_file:
        text_file.write(execution_time + " " + str(data_encode) + "\n")

    # Break the loop for exiting the program via keyhandling
    if keyboard.is_pressed('s'):
        break


