import serial
import time
import matplotlib
matplotlib.use("tkAgg")
import matplotlib.pyplot as plt
import numpy as np
import datetime

ser = serial.Serial('COM9', 38400, timeout=5) #timeout of 5 to give python proper time to read bits
ser.flushInput()


while True:
    #read bits from serial
    ser_bytes = ser.readline()
    #transform bytes into ascii code
    decoded_bytes = float(ser_bytes.decode("ascii"))
    print(ser_bytes.decode("ascii"))
    Outfile = open("output.txt","a+")
    Outfile.write(str(datetime.datetime.now()) + ", " + str(decoded_bytes) + '\n')

Outfile.close()
