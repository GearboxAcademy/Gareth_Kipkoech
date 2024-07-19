from machine import SoftSPI,ADC,Pin
import ssd1306
from mfrc522 import MFRC522
from time import sleep

#Initializing the card reader
reader = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0)
cards=["1497272400"]
 
print("Bring TAG closer...")
print("")

#initializing the OLED Display
spi=SoftSPI(baudrate=50000,polarity=1,sck=Pin(14),mosi=Pin(13),miso=Pin(12))
dc = Pin(6)   # data/command
rst = Pin(5)  # reset
cs = Pin(15)  # chip select, some modules do not have a pin for this

display = ssd1306.SSD1306_SPI(128, 64, spi, dc, rst, cs)

#initializing the relay and green led
relay=Pin(11,Pin.OUT)
greenLed=Pin(10,Pin.OUT)

#initializing the buzzer
buzzer=Pin(9,Pin.OUT)

x=50
y=0
z=1
diff=5
    
while True:
    display.fill(0)
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            display.text('CARD ID: '+str(card),0,0,1)
            if str(card) in cards:
                print("Access granted")
                display.text("Access granted!",0,10,1)
                display.show()
                relay.value(1)
                greenLed.value(1)
                sleep(2)
                relay.value(0)
                greenLed.value(0)
                display.fill(0)
            else:
                print("Access denied")
                display.text("Access DENIED!",0,10,1)
                greenLed.value(1)
                display.show()
                buzzer.value(1)
                sleep(3)
                buzzer.value(0)
                display.fill(0)
    else:
        display.text("BRING",x,y,z)
        display.text("CARD",x+2,y+10,z)
        display.text("CLOSER",x-4,y+20,z)
        y=y+diff
        if y>=35 or y<=0:
            diff=diff*-1
        display.show()
    sleep(1)
