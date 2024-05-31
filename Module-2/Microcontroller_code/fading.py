from machine import Pin,PWM,ADC
from time import sleep

ledPin=PWM(Pin(26))
ledPin.freq(1000)
ledPin.duty_u16(0)
potPin=ADC(Pin(27))


i=0;
diff=1000
while True:
    potVal=potPin.read_u16()
    print(potVal)
    ledPin.duty_u16(potVal)
    sleep(0.1)
