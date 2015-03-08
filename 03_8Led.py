import RPi.GPIO as GPIO
from GPIOlib import wP2board
from time import sleep
from random import randint

def led_on(wPpin):
    try:
        GPIO.output(wP2board(wPpin),GPIO.LOW)
    except:
        pass

def led_off(wPpin):
    try:
        GPIO.output(wP2board(wPpin),GPIO.HIGH)
    except:
        pass

## setup 

led_count = 8

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

for i in range(0,led_count):
    GPIO.setup(wP2board(i),GPIO.OUT, initial=GPIO.HIGH)

## Back n forth

print "Back and forth"

for runcount in range(0,3):

    for i in range(0,led_count):  ## 0 to led_count-1
        led_on(i)
        sleep(0.100)
        led_off(i)
    ## sleep(0.500)
    for i in range(led_count-1,-1,-1): ## led_count-1 to 0
        led_on(i)
        sleep(0.100)
        led_off(i)

## chase

print "Chase"

for runcount in range(0,20):

    for i in range(0,3):
        for j in range(i,led_count,3):
            led_on(j)
        sleep(0.100)
        for j in range(i,led_count,3):
            led_off(j)

## sweep

print "Sweep"

for runcount in range(0,3):

    for i in range(0,led_count):  ## 0 to led_count-1
        led_on(i)
        sleep(0.050)
    for i in range(0,led_count):  ## 0 to led_count-1
        led_off(i)
        sleep(0.050)
    for i in range(led_count-1,-1,-1): ## led_count-1 to 0
        led_on(i)
        sleep(0.050)
    for i in range(led_count-1,-1,-1): ## led_count-1 to 0
        led_off(i)
        sleep(0.050)

## Random

print "Random"

for runcount in range(0,3):
    
    for i in range(0,20):
        j = randint(0,led_count-1)
        led_on(j)
        sleep(0.100)
        led_off(j)
        
## Pair

print "Pair"

for runcount in range(0,3):

    for i in range(0,led_count):  ## 0 to led_count-1
        led_on(i)
        sleep(0.100)
        led_off(i-1)
    sleep(0.100)

    for i in range(led_count-1,-1,-1): ## led_count-1 to 0
        led_on(i)
        sleep(0.100)
        led_off(i+1)
    sleep(0.100)

led_off(0)

## VU Meter

print "VU Meter"

for runcount in range(0,3):

    for i in range(0,25): 
        j = randint(0,led_count-1)
        for k in range(0,j+1):  ## 0 to j
            led_on(k)
            sleep(0.02)
        for k in range(led_count-1,j,-1): ## led_count-1 to j
            led_off(k)
            sleep(0.02)
    for i in range(led_count-1,-1,-1): ## led_count-1 to 0
        led_off(i)


### Ticker

print "Ticker"

array = []
for i in range(0,led_count):
    array.append(GPIO.HIGH)

for runcount in range(0,3):

    def draw_array():
        for i in range(0,len(array)):
	    GPIO.output(wP2board(i),array[i])

    def shift_array():
        for i in range(len(array)-1,0,-1):
            array[i] = array[i-1]

    for i in range(0,25):
        shift_array()
        array[0] = randint(GPIO.LOW,GPIO.HIGH)
        draw_array()
        sleep(0.120)

### Center Swipe

print "Center Swipe"

center = (led_count/2) -1

for i in range(led_count-1,-1,-1): ## led_count-1 to 0
    led_off(i)

for runcount in range(0,3):
    step = 1
    for i in range(center,-1,-1):
         led_on(i)
         led_on(i+step)
         sleep(0.200)
         step += 2
    step = 1
    for i in range(center,-1,-1):
         led_off(i)
         led_off(i+step)
         sleep(0.200)
         step += 2
    
        

GPIO.cleanup()

