import threading
import time
import serial
import sys
import keyboard
import numpy as np
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def readSerialData(ser):
    while True:
        data_raw = ser.readline()
        data_encode = data_raw.decode('ascii').strip()

        if data_encode.isdigit():
            databufffer.append(int(data_encode))
            print(databufffer)
        
        if keyboard.is_pressed('s'):
            break

def animate(i):
    line.set_data(range(plotLength), databufffer)
    return line,

isConnected = False
plotLength = 100
databufffer = collections.deque([0] * plotLength, maxlen=plotLength)

try:
    ser = serial.Serial( port='COM3', baudrate=9600, parity=serial.PARITY_NONE, 
    stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)
    isConnected = True
except serial.SerialException:
    print("Error while connecting to port COM 3")
    sys.exit()

reader_thread = threading.Thread(target=readSerialData, args=(ser,), name='daemon')
# reader_thread.setDaemon(True)
reader_thread.start()    

time.sleep(0.1)
if isConnected:
    fig = plt.figure()
    ax = plt.axes(xlim=(0,100), ylim=(0,1000))
    ax.set_xlabel("Time")
    ax.set_ylabel("Analog Value")
    max_points = 150
    
    line, = ax.plot(np.arange(max_points), np.ones(max_points, dtype=np.float)*np.nan, lw=2)
    anim = animation.FuncAnimation(fig, animate, interval=50)
    plt.show()

