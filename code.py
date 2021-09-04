# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import digitalio
import usb_hid

from adafruit_hid.gamepad import Gamepad

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

gp = Gamepad(usb_hid.devices)

pin1 = digitalio.DigitalInOut(board.GP1)
pin1.switch_to_input(pull=digitalio.Pull.UP)
#pin2 = digitalio.DigitalInOut(board.GP2)

while True:
    led.value = not pin1.value

    # Buttons are grounded when pressed (.value = False)
    if not pin1.value:
        gp.press_buttons(1)
    else:
        gp.release_buttons(1)
