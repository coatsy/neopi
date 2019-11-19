import board
import neopixel
import time

numPixels = 12

pixels = neopixel.NeoPixel(board.D12, numPixels, auto_write=False)

pixels[0] = (0,0,0)

for pixel in range(0, numPixels*10):
    for incr in range(0,5):
        pixels[(pixel+incr) % numPixels] = (incr*8,0,0)
    pixels.show()
    time.sleep(0.01)

