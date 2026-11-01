import time
import _thread
from machine import Pin
from ssd1306 import SSD1306_I2C
from utils.menu_utils import draw_script_running_menu
from utils.check_button import check_button

led = Pin(25, Pin.OUT)


def main(display: SSD1306_I2C, button_exit: Pin, options: list[str], name: str):
    draw_script_running_menu(display, name)

    _thread.start_new_thread(check_button, (button_exit,))

    while True:
        led.value(0)
        time.sleep_ms(500)
        led.value(1)
        time.sleep_ms(500)