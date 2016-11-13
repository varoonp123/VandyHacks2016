# @Author: Varoon Pazhyanur <Varoon>
# @Date:   12-11-2016
# @Last modified by:   Varoon
# @Last modified time: 11-12-2016


#GOAL: Take in serial signals from 3 sensors via arduino and push that data to Initial State Data Bucket.
import time
from ISStreamer.Streamer import Streamer
import serial
import os

#Define streamer object to push data to Initial State
streamer = Streamer(bucket_key = "PQRLV86HNMS7",access_key="et2FqaeesA6KtWNxufN8smIRLQebb4z7")
#Define arrays to hold 10 most recent serial signals from each Sensor
"""
sens1 = [None]*10
sens2 = [None]*10
sens3 = [None]*10
#Find used USB Serial Port
for i in range(0,11):
    string = '/dev/ttyUSB{}'.format(i)
    try:
        ser=serial.Serial(string,9600)
        break
    except Exception as e:
        continue
    print 'Could not find the serial port'
print ser.name

while true:
    s=int(ser.read(1))  #read 1 byte
    if abs(s)==1:
        sens1[:-1] = sens1[1:]
        sens2[11] = s
    elif abs(s)==2:
        sens2[:-1] = sens1[1:]
        sens2[11] = s
    elif abs(s)==3:
        sens3[:-1] = sens1[1:]
        sens3[11] = s
    else:
        print("INVALID SIGNAL %d"%{s})
"""
for i in range(1,4):
    streamer.log("Sensor{0}".format(i),1)
    time.sleep(5)
    streamer.log("Sensor{0}".format(i),0)
