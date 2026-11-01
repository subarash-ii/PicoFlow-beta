import time
import machine
from machine import Pin


def check_button(button: Pin):
    time.sleep_ms(50)

    while True:
        if button.value() == 0:
            time.sleep_ms(30)

            if button.value() == 0:
                machine.reset()

        time.sleep_ms(100)