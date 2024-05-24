from machine import Pin
from time import sleep

led=Pin(26,Pin.OUT)
print("Hello World")

while True:
    led.value(1)
    sleep(1)
    led.value(0)
    sleep(1)
    