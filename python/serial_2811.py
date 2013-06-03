import serial
import time
#from random import randint

numleds = 60
teensy = serial.Serial('/dev/tty.usbmodem11571', 115200)
time.sleep(2)

led_list = []

for x in range(numleds):
    led_list.append(255)
    led_list.append(255)
    led_list.append(0)

teensy.write(bytearray(led_list))
time.sleep(2)

led_list = []
for x in range(numleds):
    led_list.append(0)
    led_list.append(255)
    led_list.append(0)

teensy.write(bytearray(led_list))
time.sleep(2)

led_list = []
for x in range(numleds):
    led_list.append(0)
    led_list.append(0)
    led_list.append(255)

teensy.write(bytearray(led_list))
time.sleep(2)

def setPixel(pixel, r, g, b):
    led_list[pixel*3] = r
    led_list[pixel*3+1] = g
    led_list[pixel*3+2] = b
    
def update():
    teensy.write(bytearray(led_list))

for x in range(numleds):
    if x % 2:
        setPixel(x,255,255,255)
update()

time.sleep(10)
teensy.close()
