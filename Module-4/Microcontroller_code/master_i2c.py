# Raspberry Pi Pico (Master) - MicroPython

from machine import Pin, SoftI2C
import time

# Initialize I2C communication
i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

# I2C slave address of the ESP32
slave_address = 0x42

def send_data_to_slave(data):
    try:
        i2c.writeto(slave_address, data)
        print(f"Sent data to slave: {data}")
    except OSError:
        print("Error sending data to slave.")

def main():
    while True:
        # Example: Send a byte (0xAA) to the slave
        send_data_to_slave(b'\xAA')
        time.sleep(1)

if __name__ == "__main__":
    main()
