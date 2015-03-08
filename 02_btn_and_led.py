import RPi.GPIO as GPIO

led_pin = 11
btn_pin = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin,GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(btn_pin,GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    GPIO.output(led_pin,GPIO.HIGH)
    if GPIO.input(btn_pin) == GPIO.LOW:
        GPIO.output(led_pin,GPIO.LOW)

GPIO.cleanup()
