#!/usr/bin/env python3

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
from flask import render_template
from flask import url_for

import json
import runpy

app= Flask(__name__)

computers= [{
    "brand": "HP",
    "processor": "Intel I7",
    "ram": 16,
    "weight": "2 pounds",
    "style": [
        "14-inch",
        "laptop",
        "touchscreen",
        "thin"
              ]
             }]

@app.route("/list/<computers>")
def yourcom(computers):
    return f"Your favorite brand is {computers}! We have added your computer to the JSON list.\n"

@app.route("/")
@app.route("/<com>")
@app.route("/home/<com>")
def collection(com):
    return render_template("index.html", computer = com)
@app.route("/jsonlist", methods=["GET","POST"])
def index():
    if request.method == 'POST':
        data = request.json
        if data:
           data= json.loads(data)
           brand = data["brand"]
           processor = data["processor"]
           ram  = data["ram"]
           weight = data["weight"]
           style = data["style"]
           computers.append({"brand":brand,"processor":processor,"ram":ram,"weight":weight, "style":style})

    return jsonify(computers)
@app.route("/login", methods = ["POST", "GET"])
def login():

    if request.method == "POST":
        if request.form.get("com") in ("Dell", "HP", "Samsung", "Apple"):
            user_com = request.form.get("com")
            if request.form.get("com") == "Dell":
                runpy.run_path("./alta3research-request01.py")
            elif request.form.get("com") == "HP":
                runpy.run_path("./alta3research-request02.py")
            elif request.form.get("com") == "Samsung":
                runpy.run_path("./alta3research-request03.py")
            else:
                runpy.run_path("./alta3research-request04.py")
            return redirect(url_for("yourcom", computers = user_com))
        else:
            user_com = "unknown brand"
            return redirect("./home")

    elif request.method == "GET":
        if request.form.get("com") in ("Dell", "HP", "Samsung", "Apple"):
            user_com = request.form.get("com")
            if request.form.get("com") == "Dell":
                runpy.run_path("./alta3research-request01.py")
            elif request.form.get("com") == "HP":
                runpy.run_path("./alta3research-request02.py")
            elif request.form.get("com") == "Samsung":
                runpy.run_path("./alta3research-request03.py")
            else:
                runpy.run_path("./alta3research-request04.py")
            return redirect(url_for("yourcom", computers = user_com))
        else:
            user_com = "unknown brand"
            return redirect("./home")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
