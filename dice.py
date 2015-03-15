import RPi.GPIO as GPIO
from GPIOlib import wP2board
from time import sleep
import sys
from random import randint

SDI   = wP2board(0)   ## serial data input
RCLK  = wP2board(1)   ## memory clock input(STCP)
SRCLK = wP2board(2)   ## shift register clock input(SHCP)

TOUCH_PIN = wP2board(3)  ## button

SegCode = [0x06,0x5b,0x4f,0x66,0x6d,0x7d]  ## six faces of the die

flag = False;


def hc595_shift(dat):
	for i in range(0,8):
		GPIO.output(SDI, 0x80 & (dat << i))
		GPIO.output(SRCLK,GPIO.HIGH)
		sleep(0.001)
		GPIO.output(SRCLK,GPIO.LOW)

	GPIO.output(RCLK,GPIO.HIGH)
	sleep(0.001)
	GPIO.output(RCLK,GPIO.LOW)

def button_press(channel):
	global flag ##  use the global variable
	flag = True 

## Inititalize

print 'GPIO.VERSION:', GPIO.VERSION

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup([SDI,RCLK,SRCLK],GPIO.OUT)   ## make pins output
GPIO.setup(TOUCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

GPIO.output([SDI,RCLK,SRCLK],GPIO.LOW)  ## set low to start

GPIO.add_event_detect(TOUCH_PIN, 
	                  GPIO.FALLING, 
	                  callback=button_press, 
	                  bouncetime=300) ## Bouncetime helps separate a push from noise.
                                      ## Not included in the original C program

## Roll the die

while True:

	if flag:
		num = randint(0,5)
		hc595_shift(SegCode[num])
		sleep(2.000)
		flag = False

	for i in range(0,6):
		hc595_shift(SegCode[i])
		sleep(0.060)


print "Cleanup"
GPIO.cleanup()