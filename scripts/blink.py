import time
from machine import Pin

led = Pin(25, Pin.OUT)

while True:
    led.value(0)
    time.sleep_ms(500)
    led.value(1)
    time.sleep_ms(500)