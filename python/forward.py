import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

GPIO.output(17, 1);
GPIO.output(18, 0);
GPIO.output(22, 0)
GPIO.output(23, 1)
time.sleep(0.5);
GPIO.output(17, 0)
GPIO.output(18, 0)
GPIO.output(22, 0);
GPIO.output(23, 0);
GPIO.cleanup()
