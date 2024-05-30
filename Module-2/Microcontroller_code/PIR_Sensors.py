from machine import Pin
import utime

#initialize the OLED display
spi = SoftSPI(baudrate=500000, polarity=1, phase=0, sck=Pin(14), mosi=Pin(13), miso=Pin(12))

dc = Pin(6)   # data/command
rst = Pin(5)  # reset
cs = Pin(15)  # chip select, some modules do not have a pin for this
display = ssd1306.SSD1306_SPI(128, 64, spi, dc, rst, cs)

#initialize the green led and buzzer
buzzer=Pin(0,Pin.OUT)
LED2=Pin(1,Pin.OUT)
PIR=Pin(16,Pin.IN,Pin.PULL_DOWN)

while True:
    display.fill(0)
    if PIR.value()==1:
        display.text("Motion Detected ! ! ",1,1,1)
        buzzer.value(1)
        LED2.value(0)
    else:
        display.text("NO Motion Detected ! ! ",1,1,1)
        LED2.value(1)
        buzzer.value(0)
        
    utime.sleep(0.5)
        