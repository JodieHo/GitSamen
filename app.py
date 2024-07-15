from flask import Flask
import felix
import appJodie

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/anders")
def anders():
    return "<p>Een hele andere wereld</p>"

@app.route("/felix1")
def felixfunctie1():
    return felix.functievanfelix()

@app.route("/Jodie1")
def JodieFunctie():
    return appJodie.functieJodie()

@app.route("/Jodie2/<destad>")
def JodieFunctie2(destad):
    return appJodie.functieJodie2(destad)