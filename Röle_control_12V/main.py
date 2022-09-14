import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
ROL = 25
GPIO.setup(ROL, GPIO.OUT)
try:
    while (True):
        GPIO.output(ROL, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.output(ROL,GPIO.HIGH)
    GPIO.cleanup()













