# @Author: Varoon Pazhyanur <Varoon>
# @Date:   11-12-2016
# @Last modified by:   Varoon
# @Last modified time: 11-12-2016

import serial
import time
import pyrebase
from  multiprocessing import Process
from ISStreamer.Streamer import Streamer

#Receives signals from distance sensors every second. The signals are +-i where i is the sensor, positive is unobstructed and negative is obstructed
#Pushes data to firebase and Initial State Data Bucket whenever there is a change
def dist_sensor_loop():
    time_cur = time.time()
    sens1=False
    sens2=False
    sens3=False
    count = 0
    while True:
        s = int(ser.readline())
        if abs(s)==1 and sens1 is not  (s<0):
            sens1 = not sens1
            db.child("sensors").child("sensor1").update({"open":sens1})
            if s<0:
                streamer.log("Sensor1",0)
            else:
                streamer.log("Sensor1",1)


        if abs(s)==2 and sens2 is not  (s<0):
            sens2 = not sens2
            db.child("sensors").child("sensor2").update({"open":sens2})
            if s<0:
                streamer.log("Sensor2",0)
            else:
                streamer.log("Sensor2",1)
        if abs(s)==3 and sens3 is not  (s<0):
            sens3 = not sens3
            db.child("sensors").child("sensor3").update({"open":sens3})
            if s<0:
                streamer.log("Sensor3",0)
            else:
                streamer.log("Sensor3",1)
#This receives arduino signals every 2 seconds with the first 4 numbers being the temp (multiplied by 100 to keep 2 decimal places of precision)
#And the last 3 digits being the traffic in that time period
#The total value is 3 bytes
#Pushes both values to the Initial State Data Bucket
def ir_temp_loop():
    t = time.time()
    s = int(ser2.readline())
    streamer.log("Temp" , float(int(s/1000)/100))
    streamer.log("Traffic", s%1000)
dist_port="/dev/cu.HC-06-DevB"
ir_port = "/dev/cu.HC-06-DevB-1"
#Configure and authenticate firebase DB.
config = {
    "apiKey": "AIzaSyCaOfxIEzUjDLBBkWhOuiN5R4t2s8LsEKY",
    "authDomain": "testproj-28fe9.firebaseapp.com",
    "databaseURL": "https://testproj-28fe9.firebaseio.com",
    "storageBucket": "testproj-28fe9.appspot.com",
    #"serviceAccount": "service_acct.json"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
#stream to Initial State API
streamer = Streamer(bucket_key = "PQRLV86HNMS7",access_key="et2FqaeesA6KtWNxufN8smIRLQebb4z7")

#instantiate serial ports

ser2=serial.Serial(dist_port,9600)
#ser2 = serial.Serial(ir_port, 9600)

#Process(target = dist_sensor_loop).start()
Process(target = ir_temp_loop).start()
