int redPin=0;
int greenPin=4;
int PIR=15;
int motionState;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("MOTION DETECTION USING ESP32");
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(PIR, INPUT);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  motionState=digitalRead(PIR);
  if(motionState){
    digitalWrite(redPin, HIGH);
    digitalWrite(greenPin, LOW);
    Serial.println("MOTION DETECTED ---- Red LED ON");
  }else{
    digitalWrite(redPin, LOW);
    digitalWrite(greenPin, HIGH);
    Serial.println("NO MOTION ---- Green LED ON");
  }
  delay(500); 
}
