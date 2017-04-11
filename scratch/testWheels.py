import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

GPIO.output(22, true)
GPIO.output(23, false)

time.sleep(2)

GPIO.output(22, false)
GPIO.output(23, false)

