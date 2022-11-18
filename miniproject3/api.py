#!/usr/bin/env python3
"""MiniProject3: receiving JSON"""

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
from flask import url_for
from flask import render_template

import json

app= Flask(__name__)

cellphone= [{
    "manufacturer": "Apple",
    "model": "Iphone 12 Pro",
    "released": 2021,
    "storage" : 500,
    "features": ["itunes","airdrop","facetime","face-unlock"]}]

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == 'POST':
        data = request.json
        if data:
           data= json.loads(data)
           manufacturer = data["manufacturer"]
           model = data["model"]
           released = data["released"]
           storage = data["storage"]
           features = data["features"]
           cellphone.append({"manufacturer":manufacturer,"model":model,"released":released,"storage":storage,"features":features})


    return jsonify(cellphone)

@app.route("/hello")
def hello():
    return "Hello, Welcome to mini project hello page"

@app.route("/success/<name>")
def success(name):
    return f"Welcome {name}\n"
@app.route("/start") # or user can land at "/start"
def start():
    return render_template("postmaker.html") # look for templates/postmaker.html
# This is where postmaker.html POSTs data to
# A user could also browser (GET) to this location
@app.route("/login", methods = ["POST", "GET"])
def login():
    # POST would likely come from a user interacting with postmaker.html
    if request.method == "POST":
        if request.form.get("nm"): # if nm was assigned via the POST
            user = request.form.get("nm") # grab the value of nm from the POST
        else: # if a user sent a post without nm then assign value defaultuser
            user = "defaultuser"
    # GET would likely come from a user interacting with a browser
    elif request.method == "GET":
        if request.args.get("nm"): # if nm was assigned as a parameter=value
            user = request.args.get("nm") # pull nm from localhost:5060/login?nm=larry
        else: # if nm was not passed...
            user = "defaultuser" # ...then user is just defaultuser
    return redirect(url_for("success", name = user)) # pass back to /success with val for name
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
