#!/usr/bin/env python
from Adafruit_CharLCD import Adafruit_CharLCD

import ADC0832
import time

def init():
	ADC0832.setup()

def loop(lcd):    
    while True:
	res = ADC0832.getResult() - 80
	if res < 0:
		res = 0
	if res > 100:
		res = 100
	print 'res = %d' % res
	lcd.clear()
	lcd.message(str(res))
	time.sleep(0.2)

if __name__ == '__main__':
        lcd = Adafruit_CharLCD()
	init()
	try:
		loop(lcd)
	except KeyboardInterrupt: 
		ADC0832.destroy()
		print 'The end !'

