import time
from urllib.parse import urlencode
import urllib
from urllib.request import Request, urlopen
import requests

code_tmp = ''
counter = 0

def getSite():
   try:
      req=urllib.request.Request("http://192.168.43.237/"); #verander naar de webserver van de arduino
      with urllib.request.urlopen(req, timeout=1) as f:
         return f.read().decode('utf-8')
   except:
      a=0
   return 'nothing'

def gelezen_barcode_uitvoeren(code):
   url = 'https://iot.zowie.online/api/authenticate' # Set destination URL here
   post_fields = {'email':'s1096181@student.hsleiden.nl','password':'spinnenpoep'}     # Set POST fields here
   request = Request(url, urlencode(post_fields).encode())
   token = urlopen(request).read().decode()
   token = token.split('"')[3]
   print(token)

   url = 'https://iot.zowie.online/api/rfid/'+code; # Set destination URL here
   #url = 'https://iot.zowie.online/api/product/'+code;
   post_fields = {'Authorization': 'Bearer '+token}
   request = Request(url, headers=post_fields,method='get')
   response = urlopen(request).read().decode()
   print(response)
   print(url +code)

if __name__ == '__main__':
   while 1==1:
      code = getSite();
      if code != 'nothing':
         if code_tmp != code:
            gelezen_barcode_uitvoeren(code)
            code_tmp = code
      if code == 'nothing':
         counter = counter + 1
         if counter == 2:
            counter = 0
            code_tmp = ''
      time.sleep(1)
