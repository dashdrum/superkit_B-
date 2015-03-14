import RPi.GPIO as GPIO
from GPIOlib import wP2board
from time import sleep
import sys

SDI   = wP2board(0)   ## serial data input
RCLK  = wP2board(1)   ## memory clock input(STCP)
SRCLK = wP2board(2)   ## shift register clock input(SHCP)

SegCode = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x77,0x7c,0x39,0x5e,0x79,0x71,0x80]


def hc595_shift(dat):
	for i in range(0,8):
		GPIO.output(SDI, 0x80 & (dat << i))
		GPIO.output(SRCLK,GPIO.HIGH)
		sleep(0.001)
		GPIO.output(SRCLK,GPIO.LOW)

	GPIO.output(RCLK,GPIO.HIGH)
	sleep(0.001)
	GPIO.output(RCLK,GPIO.LOW)

## Inititalize

print 'GPIO.VERSION:', GPIO.VERSION

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup([SDI,RCLK,SRCLK],GPIO.OUT)   ## make pins output

GPIO.output([SDI,RCLK,SRCLK],GPIO.LOW)  ## set low to start

## Display digits

for j in range(0,3):
	for i in range(0,17):
		hc595_shift(SegCode[i])
		sleep(0.500)


print "Cleanup"
GPIO.cleanup()