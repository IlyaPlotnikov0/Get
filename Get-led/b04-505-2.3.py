import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)
delitel = 6
GPIO.setup(delitel, GPIO.IN)
state = 0 

while True:
    GPIO.output(led, not GPIO.input(delitel))
    time.sleep(0.2)