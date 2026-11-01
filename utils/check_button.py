import time
import machine
from machine import Pin


def check_button(button: Pin):
    time.sleep_ms(50)

    prev_state = button.value()

    while True:
        curr_state = button.value()

        if prev_state == 1 and curr_state == 0:
            time.sleep_ms(30)

            if button.value() == 0:
                machine.reset()

        prev_state = curr_state
        time.sleep_ms(100)