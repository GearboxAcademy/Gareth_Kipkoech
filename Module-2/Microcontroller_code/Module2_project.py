from machine import Pin,PWM
import utime

#Initilizing the OLED
spi = SoftSPI(baudrate=500000, polarity=1, phase=0, sck=Pin(14), mosi=Pin(13), miso=Pin(12))

dc = Pin(6)   # data/command
rst = Pin(5)  # reset
cs = Pin(15)  # chip select, some modules do not have a pin for this

display = ssd1306.SSD1306_SPI(128, 64, spi, dc, rst, cs)

#Initializing the Ultrasonic and led2(Red led)
Trig=Pin(3,Pin.OUT)
Echo=Pin(2,Pin.IN)
LED2=PWM(Pin(26))
LED2.freq(1000)
LED2.duty_u16(0)

#Initializing the PIR sensor and led1(Green led)
PIR=Pin(16,Pin.IN,Pin.PULL_DOWN)
LED1=Pin(0,Pin.OUT)

#Function for detecting motion
def motion():
        display.fill(0)
        LED1.value(PIR.value())
        if PIR.value()==1:
            display.text("Motion Detected",1,1,1)
        else:
            display.text("No Motion!",1,1,1)
        utime.sleep(0.5)

#Function for measuring distance
def read_distance():
    
    Trig.value(0)
    utime.sleep_us(2)
    Trig.value(1)
    utime.sleep_us(5)
    Trig.value(0)
    while Echo.value()==0:
        Time_taken_go=utime.ticks_us()
    
    while Echo.value()==1:
        Time_taken_received=utime.ticks_us()
    
    timeTaken=Time_taken_received-Time_taken_go
    distance=((0.0343*timeTaken)/2)
    brightness=(65550/150)*distance
    LED2.duty_u16(int(brightness))
    display.fill(0)
    display.text("The distance object is "+distance+" cm away",1,1,1)

while True:
    read_distance()
    motion()
    utime.sleep(1)