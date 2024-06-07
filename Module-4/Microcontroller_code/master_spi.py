import machine
from machine import Pin
from time import sleep


led=machine.Pin(25,Pin.OUT)
# Configure SPI pins
spi_sck = Pin(18)
spi_tx = Pin(19)
spi_rx = Pin(16)
slave_select_pin = Pin(10, Pin.OUT)

# Initialize SPI as master
spi = machine.SPI(0, baudrate=9600, polarity=0, phase=0, sck=spi_sck, mosi=spi_tx, miso=spi_rx)

while True:
    # Select the slave (assert CS)
    slave_select_pin.value(0)
    led.value(1)
    sleep(1)
    # Send data to the slave
    tx_data = b'\x10'
    spi.write(tx_data)
    print("Sent data from master: ",tx_data[0])

    # Receive data from the slave
    rx_data = spi.read(1)
    
    # Deselect the slave (deassert CS)
    slave_select_pin.value(1)
    led.value(0)

    print("Received data from slave:", rx_data[0])
    
    sleep(1)
    
    
