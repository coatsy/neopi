import board
import neopixel
import time

# from https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/blob/master/examples/neopixel_rpi_simpletest.py

PIXEL_PIN = board.D18
ORDER = neopixel.RGB
num_pixels = 300

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def snake(r,g,b):
    for pixel in range(0, num_pixels):
        for incr in range(0,5):
            pixels[(pixel+incr) % num_pixels] = (int(incr*r/5),int(incr*g/5),int(incr*b/5))
        pixels.show()

def clear():
    pixels.fill((0,0,0))
    pixels.show()

pixels = neopixel.NeoPixel(board.D18, num_pixels, auto_write=False)

snake(128,0,0)

time.sleep(1)

rainbow_cycle(0)

clear()

