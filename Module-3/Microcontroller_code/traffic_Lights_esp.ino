
int red=0;
int green=2;
int yellow=4;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("Hello, ESP32!");
  pinMode(red, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(green, OUTPUT);

  digitalWrite(red,LOW);
  digitalWrite(yellow,LOW);
  digitalWrite(green,LOW);
  delay(1000);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(red,HIGH);
  digitalWrite(yellow,LOW);
  digitalWrite(green,HIGH);
  Serial.println("Start BRAKING !");
  delay(1000);
  
  digitalWrite(red,HIGH);
  digitalWrite(yellow,LOW);
  digitalWrite(green,LOW);
  Serial.println("STOP !");
  delay(2000);

  digitalWrite(red,HIGH);
  digitalWrite(yellow,HIGH);
  digitalWrite(green,LOW);
  Serial.println("Remove your hand brakes");
  delay(1000);

  digitalWrite(red,LOW);
  digitalWrite(yellow,HIGH);
  digitalWrite(green,LOW);
  Serial.println("WAIT !");
  delay(2000);
  

  digitalWrite(red,LOW);
  digitalWrite(yellow,HIGH);
  digitalWrite(green,HIGH);
  Serial.println("Start your engines !");
  delay(1000);

  digitalWrite(red,LOW);
  digitalWrite(yellow,LOW);
  digitalWrite(green,HIGH);
  Serial.println("GO !");
  delay(2000); 
}
