from machine import Pin
import time

# Pin setup
led = Pin(17, Pin.OUT)  # LED pin
button = Pin(21, Pin.IN, Pin.PULL_UP)  # Button pin with internal pull-up

while True:
    if button.value() == 0:  # Button pressed (logic LOW)
        led.value(1)  # Turn on LED
    else:
        led.value(0)  # Turn off LED
    time.sleep(0.1)  # Small delay for debounce
