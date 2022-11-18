#!/usr/bin/env python3
"""DEMO: receiving JSON"""

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify

import json

app= Flask(__name__)

cellphones= [{
    "manufacturer": "Apple",
    "model": "Iphone 12 Pro",
    "released": 2021,
    "storage" : 500,
    "features": [
        "wifi",
        "bluetooth",
        "speakerphone",
        "face-unlock"
              ]
             }]

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == 'POST':
        data = request.json
        if data:
           data= json.loads(data)
           manufacturer = data["manufacturer"]
           model = data["realName"]
           released = data["released"]
           features = data["features"]
           cellphonedata.append({"manufacturer":manufacturer,"model":model,"released":released,"features":features})

    return jsonify(cellphonedata)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
