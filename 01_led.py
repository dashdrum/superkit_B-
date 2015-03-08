from time import sleep
import RPi.GPIO as GPIO

led_pin = 11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin,GPIO.OUT, initial=GPIO.HIGH)

while True:
    GPIO.output(led_pin,GPIO.LOW)
    sleep(0.5)
    GPIO.output(led_pin,GPIO.HIGH)
    sleep(0.5)

GPIO.cleanup()
