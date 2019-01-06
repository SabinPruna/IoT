from Adafruit_CharLCD import Adafruit_CharLCD
from TweeterBot import TweeterBot

from time import sleep
import RPi.GPIO as GPIO
import time
import datetime


#-----------------TEMPERATURE HUMIDITY SENSOR----------------------#
channel = 22
data = []
j = 0

#pins used in program are their physical numbering not their GPIO BCM name
GPIO.setmode(GPIO.BOARD)

time.sleep(1)

GPIO.setup(channel, GPIO.OUT)

GPIO.output(channel, GPIO.LOW)
time.sleep(0.02)
GPIO.output(channel, GPIO.HIGH)

GPIO.setup(channel, GPIO.IN)

while GPIO.input(channel) == GPIO.LOW:
	continue

while GPIO.input(channel) == GPIO.HIGH:
	continue

while j < 40:
	k = 0
	while GPIO.input(channel) == GPIO.LOW:
		continue

	while GPIO.input(channel) == GPIO.HIGH:
		k += 1
		if k > 100:
			break

	if k < 8:
		data.append(0)
	else:
		data.append(1)

	j += 1

print ("sensor is working.")
print (data)

humidity_bit = data[0:8]
humidity_point_bit = data[8:16]
temperature_bit = data[16:24]
temperature_point_bit = data[24:32]
check_bit = data[32:40]

humidity = 0
humidity_point = 0
temperature = 0
temperature_point = 0
check = 0

for i in range(8):
	humidity += humidity_bit[i] * 2 ** (7 - i)
	humidity_point += humidity_point_bit[i] * 2 ** (7 - i)
	temperature += temperature_bit[i] * 2 ** (7 - i)
	temperature_point += temperature_point_bit[i] * 2 ** (7 - i)
	check += check_bit[i] * 2 ** (7 - i)

tmp = humidity + humidity_point + temperature + temperature_point

if check == tmp:
	print ("temperature : ", temperature, ", humidity : " , humidity)
else:
	print ("wrong")
	print ("temperature : ", temperature, ", humidity : " , humidity, " check : ", check, " tmp : ", tmp)

GPIO.cleanup()
#-----------------TEMPERATURE HUMIDITY SENSOR----------------------#


def loop():
    tweeter = TweeterBot()
    lcd = Adafruit_CharLCD()
    
    while True:        
        lcd.clear()
        lcd.message("temperature  "+ str(temperature))
        sleep(2)
        lcd.clear()
        lcd.message("humidity " + str(humidity))
        sleep(2)	
        tweeter.send_tweet("temperature  "+ str(temperature) +  " humidity " + str(humidity) + " check " + str(check) + " timestamp: " + str(datetime.datetime.now()))      
		
if __name__ == '__main__':
	loop()		