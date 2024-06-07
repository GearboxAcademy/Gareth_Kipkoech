#include <SPI.h>

const int slaveSelectPin = 5; // GPIO pin connected to slave select (CS)
const int led=2;
void setup() {
    Serial.begin(9600);
    pinMode(slaveSelectPin, OUTPUT);
    pinMode(led,OUTPUT);
    
    SPI.begin(); // Initialize SPI
    digitalWrite(led,LOW);
    digitalWrite(slaveSelectPin,HIGH);
    delay(1000);
}

void loop() {
    // Wait for the master to select the slave (CS low)
    while (digitalRead(slaveSelectPin)) {
        Serial.print("Waiting .... ");
        Serial.println(digitalRead(slaveSelectPin));
        digitalWrite(led,HIGH);
        delay(1000);
    }
    // Send response back to the master
    uint8_t txData = 0x12;
    uint8_t rxData=SPI.transfer(txData);
    Serial.print("Sent data from slave: ");
    Serial.println(txData);

    // Receive data from the master
    Serial.print("Received data from master: ");
    Serial.println(rxData);
    // Process received data (e.g., perform an action)

    

    // Wait for the master to deselect the slave (CS high)
    while (!digitalRead(slaveSelectPin)) {
        digitalWrite(led,LOW);
        Serial.print("DESELECTING .... ");
        Serial.println(digitalRead(slaveSelectPin));
        delay(1000);
    }
    Serial.println("---------------------------");
}

