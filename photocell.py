import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(19,GPIO.IN)
x = 0

while (x == 0)
    while (GPIO.input(19) == 0):

       
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(21,GPIO.HIGH)
        GPIO.output(18,GPIO.HIGH)
        
    while (PIO.input(19) == 1):

        GPIO.output(21,GPIO.LOW)
        GPIO.output(16,LOW)
        GPIO.output(18,GPIO.LOW)