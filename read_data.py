import serial
import time
ser = serial.Serial('/dev/cu.usbmodem14964401', 115200)
import numpy as np

data = []
length = 10
hz = 25
for i in range(length*hz):
    b = ser.readline()
    data.append(parse_data(b))
    time.sleep(1/hz)
ser.close