#!/usr/bin/env python3
import requests
import json
from pprint import pprint

URL= "http://127.0.0.1:2224/"

new_cellphone= {
    "manufacturer": "Google",
    "model": "Pixel 7 Pro",
    "released": 2020,
    "storage" : 128,
    "features": [
        "NFC",
        "hiddenfolders",
        "Android 9",
        "fingerprint-unlock"
              ]
             }

# json.dumps takes a python object and returns it as a JSON string
new_cellphone= json.dumps(new_cellphone)

# requests.post requires two arguments at the minimum;
# a url to send the request 
# and a json string to attach to the request
resp= requests.post(URL, json=new_cellphone)

# pretty-print the response back from our POST request
pprint(resp.json())
