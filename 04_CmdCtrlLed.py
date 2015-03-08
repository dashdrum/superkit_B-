import RPi.GPIO as GPIO
from GPIOlib import wP2board
import sys

def cmdctrlled(pin,state):

    pin = int(pin)
    state = int(state)

    ## setup 
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(wP2board(pin),GPIO.OUT)

    ## set LED pin value
    GPIO.output(wP2board(pin),state)

if __name__ == '__main__':

    try:
        pin = sys.argv[1]
        state = sys.argv[2]
    except IndexError:
        print "Please supply 2 parameters, pin and state"
    except others:
        raise

    cmdctrlled(pin,state)

