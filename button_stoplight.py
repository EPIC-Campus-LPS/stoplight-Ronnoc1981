import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(19,GPIO.IN)
x = 0

while(x == 0)
    if (GPIO.input(19) == 0):
        print ("stoplight on")
        # green light code
        GPIO.output(16,GPIO.HIGH)
        time.sleep(5)
        GPIO.output(16,LOW)
        # yellow light code
        GPIO.output(21,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(21,GPIO.LOW)
        # red light code
        GPIO.output(18,GPIO.HIGH)
        time.sleep(4)
        GPIO.output(18,GPIO.LOW)
        print ("stoplight off")