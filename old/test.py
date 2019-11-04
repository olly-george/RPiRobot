import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

GPIO.output(22, 1)
GPIO.output(23, 0)
time.sleep(1);
GPIO.output(22, 0);
GPIO.output(23, 0);
GPIO.cleanup()
