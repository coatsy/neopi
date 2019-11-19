# neopi

Files for working with NeoPixels and Raspberry Pi

## Setup

### Setup for CircuitPython

[https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)

### Install adafruit neopixel library

`sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel`

Note that running the adafruit library requires root access as it reads/writes directly from/to `dev/mem`

Run a program with `sudo python3 <filename.py>`

Library docs are at [https://circuitpython.readthedocs.io/projects/neopixel/en/latest/](https://circuitpython.readthedocs.io/projects/neopixel/en/latest/)

## Useful links

[https://www.thegeekpub.com/16187/controlling-ws2812b-leds-with-a-raspberry-pi/](https://www.thegeekpub.com/16187/controlling-ws2812b-leds-with-a-raspberry-pi/)

Raspberry Pi PWM pins (from an answer at [https://forums.adafruit.com/viewtopic.php?p=445593](https://forums.adafruit.com/viewtopic.php?p=445593))

| PIN | GPIO | DMA CHANNEL |
|--|--|--|
| 12 | 18 | 0 |
| 32 | 12 | 0 |
| 33 | 13 | 1 |
| 35 | 19 | 1 |

Note that unless you use one of the pins on DMA Channel 0, you need to set the channel in the constructor of the NeoPixel object

### Good Samples

[https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel)