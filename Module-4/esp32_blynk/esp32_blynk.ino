#define BLYNK_TEMPLATE_ID "TMPL280pQpoeq"
#define BLYNK_TEMPLATE_NAME "blinkled"
#define BLYNK_AUTH_TOKEN "ZmIs2CUiuUgsSQ5Rud4iohQJVUWS-jBi"

#define BLYNK_PRINT Serial
#include <Blynk.h>
#include <BlynkSimpleEsp32.h>
#include <WiFi.h>
#include <WiFiClient.h>

// Your WiFi credentials.
const char auth[] = BLYNK_AUTH_TOKEN;
const char ssid[] = "GEARBOX MEMBERS";
const char pass[] = "Members@Gearbox";

void setup() {
    Serial.begin(9600);
    Blynk.begin(auth, ssid, pass,"blynk.cloud",80);
}

void loop() {
    Blynk.run();
    // Your other code here
}
