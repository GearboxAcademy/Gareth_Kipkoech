#include <HardwareSerial.h>

void setup() {
    Serial.begin(9600); // Initialize UART
}

void loop() {
    // Receive data from master (Raspberry Pi Pico)
    if (Serial.available()) {
        char receivedChar = Serial.read();
        // Process received data (e.g., control sensors, LEDs, etc.)
        // Send response back to the master if needed
    }
}
