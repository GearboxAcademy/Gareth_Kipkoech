// ESP32 (Slave) - C

#include <Wire.h>

// I2C address (must match the master's address)
#define SLAVE_ADDRESS 0x42

void setup() {
    Wire.begin(21,22,SLAVE_ADDRESS); // Initialize I2C as slave
    Wire.onReceive(receiveData);
    Serial.begin(115200);
}

void receiveData(int byteCount) {
    while (Wire.available()) {
        char receivedData = Wire.read();
        Serial.print("Received data from master: ");
        Serial.println(receivedData);
        // Process received data (e.g., control an LED, update sensor readings, etc.)
    }
    
}

void loop() {
    // Your code here
    // Continue processing or wait for more data from the master
}
