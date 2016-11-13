# @Author: Varoon Pazhyanur <Varoon>
# @Date:   11-12-2016
# @Last modified by:   Varoon
# @Last modified time: 11-13-2016

import serial
import time
import pyrebase
from  multiprocessing import Process
from ISStreamer.Streamer import Streamer

#Receives signals from distance sensors every second. The signals are +-i where i is the sensor, positive is unobstructed and negative is obstructed
#Pushes data to firebase and Initial State Data Bucket whenever there is a change
def dist_sensor_loop():

    #[free,taken]
    sensor1_signals=[0,0]
    sensor2_signals=[0,0]
    cur_time = time.time()
    while True:
        #ALL POSSIBLE RECEIVE SIGNALS WITH ASSOCIATED COUNTS

        s=int(ser1.readline())
        if abs(s)==1 or abs(s)==2:
            if abs(s)==1:
                sensor1_signals[0 if s<0 else 1]+=1
            if abs(s)==2:
                sensor2_signals[0 if s<0 else 1]+=1

            if time.time()-cur_time>5:
                #values to push to database and Initial State

                sens1 = 0 if sensor1_signals[0]<=1 else 1
                sens2 = 0 if sensor2_signals[0]<=3 else 1

                sensor1_signals=[0,0]
                sensor2_signals=[0,0]
                cur_time=time.time()

                db.child("sensors").child("sensor1").update({"open":sens1})
                db.child("sensors").child("sensor2").update({"open":sens2})

                streamer.log("Sensor1",sens1)
                streamer.log("Sensor2",sens2)

#This receives arduino signals every 2 seconds with the first 4 numbers being the temp (multiplied by 100 to keep 2 decimal places of precision)
#And the last 3 digits being the traffic in that time period
#The total value is 3 bytes
#Pushes both values to the Initial State Data Bucket
def ir_temp_loop():

    while True:
        s = ser2.readline().decode('utf-8')

        arr = s.split("-")
        streamer.log("Temp" , float(arr[0]))
        streamer.log("Traffic", int(arr[1]))
        db.child("Traffic").set({"val":int(arr[1])})
        db.child("Temp").set({"val":float(arr[0])})

def pressure_sensor_loop():

    cur_time = time.time()
    strain1=0
    strain2=0
    while True:
        #receive 2 vals sep by colon.
        s = ser3.readline().decode('utf-8').rstrip().split(":")

        strain1+=abs(int(s[0]))
        strain2+=abs(int(s[1]))


        if (time.time()-cur_time>=2):    #only push to Initial State and firabase every 2 seconds
            streamer.log("Strain1", strain1)
            streamer.log("Strain2", strain2)
            db.child("StrainGauge1").set({"val":strain1})
            db.child("StrainGauge2").set({"val":strain2})
            strain1=0
            strain2=0
            cur_time = time.time()




dist_port = "/dev/cu.HC-06-DevB-1"
ir_port="/dev/cu.HC-06-DevB"
pressure_port = "/dev/cu.HC-06-DevB-2"

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
print("starting")
ser1=serial.Serial(dist_port,9600)
ser2 = serial.Serial(ir_port, 9600)
ser3 = serial.Serial(pressure_port, 9600)
print("Connected")
Process(target = dist_sensor_loop).start()
Process(target = ir_temp_loop).start()
Process(target = pressure_sensor_loop).start()
