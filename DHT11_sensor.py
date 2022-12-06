import serial
import time

import pyrebase
import math
from datetime import datetime
from os import system
firebaseConfig = {
    "apiKey": "AIzaSyDRUEVKiQqwP_WEWqQefp3AjeJb0McqryU",
    "authDomain": "monitoring-pm.firebaseapp.com",
    "databaseURL": "https://monitoring-pm-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "monitoring-pm",
    "storageBucket": "monitoring-pm.appspot.com",
    "messagingSenderId": "552814734574",
    "appId": "1:552814734574:web:73e98f5720aa11c30717ff",
    "measurementId": "G-4FHF6FY03G"
}


firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

y = 0

serr = serial.Serial(port='/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_954373133353512091D1-if00',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0.5,
    writeTimeout=0)

serr.write(b"ready\n")
time.sleep(0.5)
while True:
    serr.write(b"ready\n")
    time.sleep(0.5)
    x = serr.readline().decode('utf-8').strip().split()
    print(x)
    if len(x):
        if x[1]=="Ready,":
            break
        else:
            pass

while True:
    try:
        y+=1
        serr.write(b"request\n")
        x = serr.readline().decode('utf-8').strip().split()
        while not len(x):
            serr.write(b"request\n")
            time.sleep(0.3)
            x = serr.readline().decode('utf-8').strip().split()
        print(x)
        data = {
            "suhu": f"{x[1]}",
            "kelembapan" : f"{x[0]}",
            "intensitas" : f"{x[2]}",
            "time" : f"{y}"
        }
        db = db.child("Monitoring").child("Kelas")
        db.set(data)
    except:
        pass