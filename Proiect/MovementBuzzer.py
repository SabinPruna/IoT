#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

BEEP_PIN = 7   # pin7
PIR_OUT_PIN = 32    # pin11
def setup():
        GPIO.setmode(GPIO.BOARD)         # Numbers pins by physical location
        GPIO.setup(BEEP_PIN, GPIO.OUT)   # Set pin mode as output
        GPIO.output(BEEP_PIN, GPIO.HIGH) # Set pin to high(+3.3V) to off the beep
        GPIO.setup(PIR_OUT_PIN, GPIO.IN)    # Set BtnPin's mode is input
    
def loop():
        while True:
            if GPIO.input(PIR_OUT_PIN) == GPIO.LOW:
                print ('...Movement not detected!')
                GPIO.output(BEEP_PIN, GPIO.LOW) 
            else:
                print ('...Movement detected!')
                GPIO.output(BEEP_PIN, GPIO.LOW)
                time.sleep(0.1)
                GPIO.output(BEEP_PIN, GPIO.HIGH)
                time.sleep(0.1)
            
def destroy():
        GPIO.output(BEEP_PIN, GPIO.HIGH)    # beep off
        GPIO.cleanup()                      # Release resource
if __name__ == '__main__':     # Program start from here
	print 'Press Ctrl+C to end the program...'
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()