import time
from machine import Pin, I2C
import ssd1306

from pins import BUTTON_UP_PIN, BUTTON_DOWN_PIN, BUTTON_SELECT_PIN, I2C_SDA_PIN, I2C_SCL_PIN
from utils.menu_utils import draw_list_menu, draw_script_running_menu
from utils.files_utils import get_scripts

button_up = Pin(BUTTON_UP_PIN, Pin.IN, Pin.PULL_UP)
button_down = Pin(BUTTON_DOWN_PIN, Pin.IN, Pin.PULL_UP)
button_select = Pin(BUTTON_SELECT_PIN, Pin.IN, Pin.PULL_UP)

i2c = I2C(0, sda=Pin(I2C_SDA_PIN), scl=Pin(I2C_SCL_PIN), freq=400000)
display = ssd1306.SSD1306_I2C(128, 64, i2c)

options = get_scripts()

selected = 0
active_button = None

start_index = 0
stop_index = 5

start_index, stop_index = draw_list_menu(display, options, selected, start_index, stop_index)

while True:
    if active_button is None:
        if button_up.value() == 0:
            time.sleep_ms(30)

            if button_up.value() == 0:
                if selected > 0:
                    selected -= 1
                    start_index, stop_index = draw_list_menu(display, options, selected, start_index, stop_index)

                active_button = button_up

        if button_down.value() == 0:
            time.sleep_ms(30)

            if button_down.value() == 0:
                if selected < len(options) - 1:
                    selected += 1
                    start_index, stop_index = draw_list_menu(display, options, selected, start_index, stop_index)

                active_button = button_down

        if button_select.value() == 0:
            time.sleep_ms(30)

            if button_select.value() == 0:
                module = __import__(f"scripts.{options[selected]}", None, None, ["main"])
                module.main(display, button_select, options, options[selected])

                active_button = button_select

    else:
        if active_button.value() == 1:
            active_button = None

    time.sleep_ms(30)