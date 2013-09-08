/*  OctoWS2811 BasicTest.ino - Basic RGB LED Test
  Required Connections
  --------------------
    pin 2:  LED Strip #1    OctoWS2811 drives 8 LED Strips.
    pin 14: LED strip #2    All 8 are the same length.
    pin 7:  LED strip #3
    pin 8:  LED strip #4    A 100 ohm resistor should used
    pin 6:  LED strip #5    between each Teensy pin and the
    pin 20: LED strip #6    wire to the LED strip, to minimize
    pin 21: LED strip #7    high frequency ringining & noise.
    pin 5:  LED strip #8
    pin 15 & 16 - Connect together, but do not use
    pin 4 - Do not use
    pin 3 - Do not use as PWM.  Normal use is ok.

  This test is useful for checking if your LED strips work, and which
  color config (WS2811_RGB, WS2811_GRB, etc) they require.
*/

#include <OctoWS2811.h>

const int ledsPerStrip = 83;

DMAMEM int displayMemory[ledsPerStrip*6];
int drawingMemory[ledsPerStrip*6];

const int config = WS2811_GRB | WS2811_800kHz;

OctoWS2811 leds(ledsPerStrip, displayMemory, drawingMemory, config);

char serial_array[ledsPerStrip*3*2];

void setup() {
  Serial.begin(115200);
  leds.begin();
  test();
}

void loop() {
  if (Serial.available() == ledsPerStrip*3*2) {
    Serial.readBytes(serial_array, ledsPerStrip*3*2);
    for (int i = 0; i < ledsPerStrip*3*2 ; i++) {
      leds.setPixel(i, serial_array[i*3], serial_array[i*3+1], serial_array[i*3+2] );
    }
    leds.show();
  }
}

void test() {
  for (byte i = 0; i < ledsPerStrip * 2 ; i++){
    leds.setPixel(i, random(0,255), random(0,255), random(0,255));
    leds.show();
    delay(20);
    leds.setPixel(i, 0, 0, 0);
    leds.show();
  }
}
