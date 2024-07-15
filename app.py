from flask import Flask
import felix
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