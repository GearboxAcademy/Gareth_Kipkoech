from machine import Pin
from time import sleep

#initialize the led Pin and Button Pin
led=Pin(0,Pin.OUT)
Button=Pin(10,Pin.IN)
#Make the led off initially
led.value(0)

while True:
    #Check if button has been pressed.
    if Button.value():
        led.value(1)
    else:
        led.value(0)
    #Delay to ensure the is enough time between button presses to prevent the led from flickering as it reads the button state too quickly.
    sleep(0.3)
        