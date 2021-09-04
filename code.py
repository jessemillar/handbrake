import board
import digitalio
import usb_hid

from adafruit_hid.gamepad import Gamepad

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

gp = Gamepad(usb_hid.devices)

pin1 = digitalio.DigitalInOut(board.GP1)
pin1.switch_to_input(pull=digitalio.Pull.UP)

pin2 = digitalio.DigitalInOut(board.GP2)
pin2.switch_to_input(pull=digitalio.Pull.UP)

while True:
    # Buttons are grounded when pressed (.value = False)
    if not pin1.value or not pin2.value:
        led.value = True
    else:
        led.value = False

    if not pin1.value:
        gp.press_buttons(1)
    else:
        gp.release_buttons(1)

    if not pin2.value:
        gp.press_buttons(2)
    else:
        gp.release_buttons(2)
