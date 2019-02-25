import time
 
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

 
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.1)
pixels.fill((0, 0, 0))
pixels.show()

button_a = DigitalInOut(board.BUTTON_A)
button_a.direction = Direction.INPUT
button_a.pull = Pull.DOWN

RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)


count = 0

while True:
    if button_a.value:
        count += 1
        time.sleep(0.1)
    else:
        color = RED
        if count > 50:
            color = ORANGE
        if count > 100:
            color = YELLOW
        if count > 200:
            color = GREEN
        binary = '{0:010d}'.format(int(bin(count)[2:]))
        pixels_on = [int(digit) for digit in binary]
        for index, value in enumerate(pixels_on):
            if value:
                pixels[len(pixels) - (index+1)] = color
            else:
                pixels[len(pixels) - (index+1)] = (0,0,0)
