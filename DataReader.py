import serial
import time
import datetime

ser = serial.Serial(
    port='COM3',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=1)

while True:
    # reading is a string
    data = ser.readline()
    data_encode = data.decode('ascii').strip()
    print(data_encode)

    with open('output.txt', 'a') as text_file:
        text_file.write(str(data_encode) + "\n")




