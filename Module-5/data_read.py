from machine import Pin
import ssd1306
from mfrc522 import MFRC522
from time import sleep
'''
RSP Pico  |   RC522
0         |   RST
1         |   SDA
2         |   SCK
3         |   MOSI
4         |   MISO
'''
#Initializing the relay.
relay=Pin(5,Pin.OUT)

#Initializing the RFID card reader.
reader = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0)

#List of card IDs that are granted access.
cards=["1497272400"]

print("Bring TAG closer...")
print("")

while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            print("CARD ID: "+str(card))
            if str(card) in cards:
                print("Access granted")
                relay.value(1)
                sleep(1)
                relay.value(0)
            else:
                print("Access denied")
    sleep(0.5)