import time
 
import board
from digitalio import DigitalInOut, Direction, Pull

switch = DigitalInOut(board.SLIDE_SWITCH)
switch.direction = Direction.INPUT
switch.pull = Pull.UP
 
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT
 
button_a = DigitalInOut(board.BUTTON_A)
button_b = DigitalInOut(board.BUTTON_B)
button_a.direction = Direction.INPUT
button_a.pull = Pull.DOWN

button_b.direction = Direction.INPUT
button_b.pull = Pull.DOWN
 
while True:
    if (switch.value and button_a.value) or (not switch.value and button_b.value):
        led.value = True
    else:
        led.value = False
 
    time.sleep(0.01)