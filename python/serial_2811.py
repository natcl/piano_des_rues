import serial
import time
from random import randint

numleds = 60
arduino = serial.Serial('/dev/tty.usbmodem11571', 115200)
time.sleep(2)

biglist = []

for x in range(60):
	#biglist.append(x)
	biglist.append(255)
	biglist.append(255)
	biglist.append(0)
barray = bytearray(biglist)

def setPixel(pixel, r, g, b):
	arduino.write(chr(pixel)+chr(r)+chr(g)+chr(b))

arduino.write(barray)
#for led in range(numleds):
	#setPixel(led, 20, 0, 20)
	#setPixel(randint(0,59),randint(0,255),randint(0,255),randint(0,255))
time.sleep(5)
arduino.close()
