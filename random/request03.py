#!/usr/bin/env python3
import requests
import json
from pprint import pprint

URL= "http://127.0.0.1:2224/jsonlist"

new_computer1= {
           "brand": "Samsung",
           "processor": "Qualcomm Snapdragon",
           "ram": 16,
           "weight": "2 pounds",
           "style": [
               "14.6-inch",
               "tablet",
               "touchscreen",
               "multi-use" ]
          }

# json.dumps takes a python object and returns it as a JSON string
new_computer1= json.dumps(new_computer1)

# requests.post requires two arguments at the minimum;
# a url to send the request 
# and a json string to attach to the request
resp= requests.post(URL, json=new_computer1)

# pretty-print the response back from our POST request
pprint(resp.json())
