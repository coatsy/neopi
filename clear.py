import board
import neopixel

numPixels = 300

pixels = neopixel.NeoPixel(board.D18, numPixels, auto_write=False)

BLANK = (0,0,0)
pixels.fill(BLANK)

pixels.show()
