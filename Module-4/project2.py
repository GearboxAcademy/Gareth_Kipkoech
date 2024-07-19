from machine import Pin,SPI,UART
from ssd1306 import SSD1306_SPI
from mfrc522 import MFRC522
import dht 
from time import sleep

'''
RSP Pico  |   RC522
0         |   RST
1         |   SDA
2         |   SCK
3         |   MOSI
4         |   MISO
'''
#Initializing the RFID Card reader
reader = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0)
cards=["412721497"]
 
'''
RSP Pico  |  OLED
16        |  CS
17        |  DC
18        |  SCK
19        |  MOSI
20        |  RST
'''
#Initializing the OLED display.
spi = SPI(0,100000,mosi=Pin(19),sck=Pin(18))
dc = Pin(17)   # data/command
rst = Pin(20)  # reset
cs = Pin(16)  # chip select, some modules do not have a pin for this
display = SSD1306_SPI(128, 64, spi, dc, rst, cs)

#initializing the cordinates of the text in OLED display
x=50
y=0
z=1
diff=5

#Initializing the DHT11 Sensor.
sensor = dht.DHT11(Pin(28))

# Initialize UART
uart = UART(0, baudrate=9600, tx=Pin(12), rx=Pin(13))

while True:
    display.fill(0)
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            print('CARD ID: '+str(card))
            display.text('CARD ID: '+str(card),0,0,1)
            if str(card) in cards:              
                display.text("Access granted!",0,10,1)
                sensor.measure()
                temp = sensor.temperature
                hum = sensor.humidity
                temp_f = temp * (9/5) + 32.0
                #Display the temperature and humidity when access is granted.
                display.text('Temp.: %3.1f C' %temp,0,30,1)
                display.text('Temp.: %3.1f F' %temp_f,0,40,1)
                display.text('Humidity: %3.1f %%' %hum,0,50,1)
                display.show()
                
                #Send data (master to slave) when access is granted.
                temp1='Temp.: %3.1f C' %temp
                temp2='Temp.: %3.1f F' %temp_f
                humidity='Humidity: %3.1f %%' %hum
                uart.write(temp1+temp2+humidity)   
            else:
                display.text("Access DENIED!",0,10,1)
                display.show()
    else:
        display.text("BRING",x,y,z)
        display.text("CARD",x+2,y+10,z)
        display.text("CLOSER",x-4,y+20,z)
        y=y+diff
        if y>=35 or y<=0:
            diff=diff*-1
        display.show()  
    sleep(1)


