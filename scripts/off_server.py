import time
import _thread
from machine import Pin
from ssd1306 import SSD1306_I2C
import usb.device
from usb.device.keyboard import KeyboardInterface, KeyCode
from utils.keyboard_utils import KeyboardWriter
from utils.menu_utils import draw_script_running_menu
from utils.check_button import check_button
from utils.env_utils import load_env
from pins import BUTTON_UP_PIN

kb = KeyboardInterface()
usb.device.get().init(kb, builtin_driver=True)

button = Pin(BUTTON_UP_PIN, Pin.IN, Pin.PULL_UP)

print("Waiting for USB keyboard...")

while not kb.is_open():
    time.sleep_ms(100)

print("Keyboard ready")

writer = KeyboardWriter(kb)

def main(display: SSD1306_I2C, button_exit: Pin, options: list[str], name: str):
    draw_script_running_menu(display, name)

    _thread.start_new_thread(check_button, (button_exit,))

    env = load_env()

    while True:
        if button.value() == 0:
            time.sleep_ms(30)

            if button.value() == 0:
                writer.type_string("sudo shutdown now")
                time.sleep_ms(30)

                kb.send_keys([KeyCode.ENTER])
                kb.send_keys([])
                time.sleep_ms(300)

                writer.type_string(env["SERVER_PASSWORD"])
                time.sleep_ms(30)

                kb.send_keys([KeyCode.ENTER])
                kb.send_keys([])

                while button.value() == 0:
                    time.sleep_ms(10)

        time.sleep_ms(10)