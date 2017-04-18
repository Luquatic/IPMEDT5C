import time
import serial
import datetime
from urllib.parse import urlencode
import urllib
from urllib.request import Request, urlopen
import requests

ser = serial.Serial('/dev/ttyUSB0',9600)
global latest_timestamp
latest_timestamp  = time.time()
card_uid_tmp = ''

def send(uid):
        print('sending authentication')
        #### auth
        url = 'https://iot.zowie.online/api/authenticate'
        post_fields = {'email':'s1096181@student.hsleiden.nl','password':'spinnenpoep'}
        request = Request(url,urlencode(post_fields).encode())
        token = urlopen(request).read().decode()
        token = token.split('"')[3]
        print('token:')
        print(token)
        print('response:')
        url = 'https://iot.zowie.online/api/rfid/'+uid
        post_fields = {'Authorization': 'Bearer '+token}
        request = Request(url,headers=post_fields,method='get')
        response = urlopen(request).read().decode()
        print(response)


def sendDataToServer(uid,latest_timestamp):
        now = time.time()
        verschil = now - latest_timestamp
        if verschil > 1.5 :
                print (verschil,uid)
                send(uid)
        return now

while True:
        data_raw = ser.readline()
        carduid = str(data_raw)
        carduid = carduid[11:-5]
        new_time = sendDataToServer(carduid,latest_timestamp)
        latest_timestamp = new_time
