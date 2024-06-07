from machine import UART, Pin

# Initialize UART
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# Send data (master to slave)
uart.write("Hello, ESP32!")

# Receive data (slave to master)
received_data = uart.read()
print("Received data from ESP32:", received_data)
