from pyo import *
import serial
import time

arduino = serial.Serial('/dev/tty.usbmodem411', 9600)
time.sleep(2)
def setPixel(pixel, r, g, b):
        arduino.write(chr(pixel)+chr(r)+chr(g)+chr(b))

s = Server(duplex=0).boot()
a = SuperSaw(freq=[100,2000], detune=0.6, bal=0.7, mul=0.5).out()
def tolist(x):
    for pixel in x[0]:
        #print pixel[0],255-pixel[1]
        setPixel(pixel[0],255-pixel[1],0,0)
    for pixel in x[1]:
        setPixel(pixel[0],0,0,255-pixel[1])

spec = Spectrum(a, size=1024, function=tolist)
spec.setWidth(60)
spec.setHeight(255)
s.start()

while 1:
	pass