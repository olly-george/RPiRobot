from flask import Flask, render_template
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    return render_template('index.html');

@app.route("/forward", methods=["POST"])
def forward():
    GPIO.output(17, 1)
    GPIO.output(23, 1)
    time.sleep(0.4)
    GPIO.output(17, 0)
    GPIO.output(23, 0)
    return "OK"

@app.route("/backward", methods=["POST"])
def backward():
    GPIO.output(18, 1)
    GPIO.output(22, 1)
    time.sleep(0.4)
    GPIO.output(18, 0)
    GPIO.output(22, 0)
    return "OK"

@app.route("/left", methods=["POST"])
def left():
    GPIO.output(18, 1)
    GPIO.output(23, 1)
    time.sleep(0.1)
    GPIO.output(18, 0)
    GPIO.output(23, 0)
    return "OK"

@app.route("/right", methods=["POST"])
def right():
    GPIO.output(17, 1)
    GPIO.output(22, 1)
    time.sleep(0.1)
    GPIO.output(17, 0)
    GPIO.output(22, 0)
    return "OK"

@app.route("/stop", methods=["POST"])
def stop():
    GPIO.output(17, 0)
    GPIO.output(22, 0)
    GPIO.output(18, 0)
    GPIO.output(23, 0)
    return "OK"



if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')
