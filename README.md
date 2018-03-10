# NeoLamp-Micro
Mini neopixel lamp controlled by a website hosted on an ESP8266 runing Micropython.

It doesn't use any libraries that are not already included in micropython so it's very memory efficient. 

## THIS code is working!

## Setup :
### Before using my code, be sure you change the neopixel object to suit your installation.
By Default the Data pin will be set to GPIO 5 (I am using an ESP8266) and I'm using a matrix with 16 neopixels like so :

    np = npx(Pin(5), 32)
If you have problems with your neopixel matrix or strip I avise you to read Adafruit's Uberguide here : https://learn.adafruit.com/adafruit-neopixel-uberguide/the-magic-of-neopixels

#### Then you simply have to load the file on your boad. I advise you to try it in the REPL before anything
