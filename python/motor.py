import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

while (True):
    GPIO.output(18, 0)
    time.sleep(1)
    GPIO.output(17, 1);
    time.sleep(5);
    GPIO.output(17, 0)
    time.sleep(1);
    GPIO.output(18, 1);
    time.sleep(5);
GPIO.cleanup()
