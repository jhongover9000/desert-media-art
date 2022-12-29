import board
import time
import analogio
import digitalio
from rainbowio import colorwheel
import neopixel
from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.color import WHITE
import pwmio
from adafruit_motor import servo

NUM_PIXELS = 12
BRIGHTNESS = 0.3

# enable neopixels
enable = digitalio.DigitalInOut(board.D10)
enable.direction = digitalio.Direction.OUTPUT




pixelsRing = neopixel.NeoPixel(board.A5, NUM_PIXELS, brightness=BRIGHTNESS,auto_write=False)
pulse = Pulse(pixelsRing, speed=0.17, color=(255,255,255), period=16)
pixelStrip= neopixel.NeoPixel(board.A4, 12, brightness=0.2,auto_write=False)

photocell = analogio.AnalogIn(board.A1)
def analog_voltage(adc):
    return adc.value / 65535 * adc.reference_voltage

pwm = pwmio.PWMOut(board.A3, duty_cycle=2 ** 15, frequency=50)

my_servo = servo.Servo(pwm)
max_close = 150
max_open = 130
my_servo.angle = max_close

BLUE = (10, 10, 80)
#100 is open, 180 is closed
pixelStrip.fill(BLUE)

flowerOpen = False


while True:
    val = photocell.value
    volts = analog_voltage(photocell)
    print(val)
    if(val<12000):

        if(flowerOpen == False):
            for angle in range(max_close, max_open, -1):  # 0 - 180 degrees, 5 degrees at a time.
                my_servo.angle = angle
                print(angle)
                #print("moving motor")
                time.sleep(0.01)
            flowerOpen = True

        #Flowers and lights are enabled here
        #val, "There will be darkness again")

        #LIGHT
        enable.value = True
        pulse.animate()
        pixelStrip.fill(BLUE)
        #
        pixelStrip.show()
    #SERVO


    else:
#        print(val)
        enable.value = False
        if(flowerOpen):
            for angle in range(max_open, max_close, 1):  # 0 - 180 degrees, 5 degrees at a time.
                my_servo.angle = angle
                #print("moving motor")
                time.sleep(0.01)
            flowerOpen = False
        pixelsRing.fill([0,0,0])
        pixelStrip.fill([0,0,0])
        pixelsRing.show()
        pixelStrip.show()


