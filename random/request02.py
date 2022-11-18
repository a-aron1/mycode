#!/usr/bin/env python3
import requests
import json
from pprint import pprint

URL= "http://127.0.0.1:2224/jsonlist"

new_computer1= {
           "brand": "Dell",
           "processor": "Ryzen 7",
           "ram": 32,
           "weight": "3 pounds",
           "style": [
               "17.3-inch",
               "laptop",
               "touchscreen",
               "gaming" ]
          }

# json.dumps takes a python object and returns it as a JSON string
new_computer1= json.dumps(new_computer1)

# requests.post requires two arguments at the minimum;
# a url to send the request 
# and a json string to attach to the request
resp= requests.post(URL, json=new_computer1)

# pretty-print the response back from our POST request
pprint(resp.json())
