import pyrebase
import time

config = {
    "apiKey": "AIzaSyCaOfxIEzUjDLBBkWhOuiN5R4t2s8LsEKY",
    "authDomain": "testproj-28fe9.firebaseapp.com",
    "databaseURL": "https://testproj-28fe9.firebaseio.com",
    "storageBucket": "testproj-28fe9.appspot.com",
    "serviceAccount": "service_acct.json"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

#db.child("Sensor1")
#db.child("Sensor2")
#db.child("Sensor3")
"""
data = {"TimeIn": time.ctime(), "TimeOut":time.ctime()}
data2 = {"TimeIn": time.ctime()}
db.child("Sensor1").child(1).set(data)
db.child("Sensor2").child(1).set(data2)
"""
db.child("Sensor2").child("1").update({"TimeOut":time.ctime()})
