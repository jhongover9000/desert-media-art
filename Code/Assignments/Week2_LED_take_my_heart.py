# Take My Heart...
# Code by Joseph Hong
# Description: This is a small RGB light experience that is meant to
# emulate the experience of a romance through the beat
# of a heart and its color.

"""CircuitPython Essentials Internal RGB LED red, green, blue example"""
import time
import board

# import colors
from adafruit_led_animation.color import RED
from adafruit_led_animation.color import MAGENTA
from adafruit_led_animation.color import PINK
from adafruit_led_animation.color import BLACK
from adafruit_led_animation.color import BLUE
from adafruit_led_animation.color import PURPLE

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.3

# function that designates color and beat intervals
def beat(color, pauseSec, intervalSec):
    led[0] = color
    time.sleep(0.1)
    led[0] = (0, 0, 0)
    time.sleep(pauseSec)
    led[0] = color
    time.sleep(0.1)
    led[0] = (0, 0, 0)
    time.sleep(intervalSec)

# get start time
startTimeSeconds = time.monotonic()

currentTimeSeconds = 0;

while True:
    # take current time
    currentTimeSeconds = int(time.monotonic() - startTimeSeconds)
    
    # according to time, change heart phase
    # phase 1: steady
    if(currentTimeSeconds < 10):
        beat(RED, 0.25, 0.7)
    # phase 2: interest
    elif(currentTimeSeconds < 20):
        beat(MAGENTA, 0.20, 0.5)
    # phase 3: love
    elif(currentTimeSeconds < 30):
        beat(PINK, 0.1, 0.3)
    # phase 4: heartbreak
    elif(currentTimeSeconds < 35):
        beat(BLACK, 1, 1)
    # phase 5: sorrow
    elif(currentTimeSeconds < 45):
        beat(BLUE, 0.4, 1)
    # phase 6: recovery
    elif(currentTimeSeconds < 55):
        beat(PURPLE, 0.35, 0.85)
    # phase 7: steady
    else:
        beat(RED, 0.25, 0.7)
