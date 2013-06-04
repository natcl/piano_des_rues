import serial
import time
import sys

if sys.platform == 'darwin':
    serial_port = '/dev/tty.usbmodem11571'
elif sys.platform == 'linux2':
    serial_port = '/dev/ttyACM0'

numleds = 60
teensy = serial.Serial(serial_port, 115200)
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
        setPixel(x, 255, 255, 255)
update()
time.sleep(2)
for x in range(numleds):
    setPixel(x, 0, 0, 0)
update()
teensy.close()
