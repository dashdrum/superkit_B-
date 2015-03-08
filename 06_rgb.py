import RPi.GPIO as GPIO
from GPIOlib import wP2board
from time import sleep
import sys

RED_PIN = 0
GREEN_PIN = 1
BLUE_PIN = 2
PAUSE = 0.500

if __name__ == '__main__':

	def led_color_set(red_value,green_value,blue_value):
	## Convert HEX to decimal percent

		red_percent = (int(red_value,16)*100/255)
		green_percent = (int(green_value,16)*100/255)
		blue_percent = (int(blue_value,16)*100/255)
	
		red.ChangeDutyCycle(red_percent)
		green.ChangeDutyCycle(green_percent)
		blue.ChangeDutyCycle(blue_percent)

	## setup 
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(wP2board(RED_PIN),GPIO.OUT)
	GPIO.setup(wP2board(GREEN_PIN),GPIO.OUT)
	GPIO.setup(wP2board(BLUE_PIN),GPIO.OUT)

	## LED init
	red = GPIO.PWM(wP2board(RED_PIN), 100) 
	green = GPIO.PWM(wP2board(GREEN_PIN), 100) 
	blue = GPIO.PWM(wP2board(BLUE_PIN), 100) 

	##  Start with all colors off
	red.start(0)
	green.start(0)
	blue.start(0)

	for i in range(0,3):
		led_color_set('0xff','0x00','0x00') ## red
		sleep(PAUSE)
		led_color_set('0x00','0xff','0x00') ## green
		sleep(PAUSE)
		led_color_set('0x00','0x00','0xff') ## blue
		sleep(PAUSE)

		led_color_set('0xff','0xff','0x00') ## yellow
		sleep(PAUSE)
		led_color_set('0xff','0x00','0xff') ## purple
		sleep(PAUSE)
		led_color_set('0x00','0xff','0x3e') 
		sleep(PAUSE)

		led_color_set('0x94','0x00','0xd3') 
		sleep(PAUSE)
		led_color_set('0x76','0xee','0x00') 
		sleep(PAUSE)
		led_color_set('0x00','0xc5','0xcd') 
		sleep(PAUSE)

	led_color_set('0xff','0xff','0xff') ##  all on
	sleep(PAUSE*2)

	GPIO.cleanup()

