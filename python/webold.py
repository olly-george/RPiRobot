from flask import Flask
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def index():
    return "<html><body>" + \
    "<table" + \
    "<tr><td></td><td><a onclick='forward()'>Forward</a></td><td></td></tr>" + \
    "<tr><td><a onclick='left()'>Left</a></td><td></td><td><a onclick='right()'>Right</a></td></tr>" + \
    "<tr><td></td><td><a onclick='backward()'>Backward</a></td><td></td></tr>" + \
    "</table>" + \
    "<script>" + \
    "function forward(){var x = new XMLHttpRequest();x.open('GET', 'forward', true);x.send();}" + \
    "function backward(){var x = new XMLHttpRequest();x.open('GET', 'backward', true);x.send();}" + \
    "function right(){var x = new XMLHttpRequest();x.open('GET', 'right', true);x.send();}" + \
    "function left(){var x = new XMLHttpRequest();x.open('GET', 'left', true);x.send();}" + \
    "</script>" + \
    "</body></html>"

@app.route("/forward")
def forward():
    GPIO.output(17, 1)
    GPIO.output(23, 1)
    time.sleep(0.4)
    GPIO.output(17, 0)
    GPIO.output(23, 0)
    return "OK"

@app.route("/backward")
def backward():
    GPIO.output(18, 1)
    GPIO.output(22, 1)
    time.sleep(0.4)
    GPIO.output(18, 0)
    GPIO.output(22, 0)
    return "OK"

@app.route("/left")
def left():
    GPIO.output(18, 1)
    GPIO.output(23, 1)
    time.sleep(0.3)
    GPIO.output(18, 0)
    GPIO.output(23, 0)
    return "OK"

@app.route("/right")
def right():
    GPIO.output(17, 1)
    GPIO.output(22, 1)
    time.sleep(0.3)
    GPIO.output(17, 0)
    GPIO.output(22, 0)
    return "OK"




if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')
