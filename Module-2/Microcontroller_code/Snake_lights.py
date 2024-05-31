from machine import Pin
from time import sleep
i=1

while True:
    led=Pin(i,Pin.OUT)
    led.value(1)
    sleep(0.5)
    led.value(0)
    i=i+1
    if i==5:
        i=0
