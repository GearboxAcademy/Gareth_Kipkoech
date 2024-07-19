int indexZeroPin=17;
int indexZero=0;
int indexOnePin=16;
int indexOne=0;
int indexTwoPin=4;
int indexTwo=0;
int indexThreePin=0;
int indexThree=0;
int n=0;
int rem;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("Binary Counter using ESP32.");
  pinMode(indexZeroPin, OUTPUT);
  pinMode(indexOnePin, OUTPUT);
  pinMode(indexTwoPin, OUTPUT);
  pinMode(indexThreePin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
    indexZero=n%2;
    rem=n/2;
    indexOne=rem%2;
    rem=rem/2;
    indexTwo=rem%2;
    rem=rem/2;
    indexThree=rem%2;
    rem=rem/2;
    Serial.print(n);
    Serial.print(" [ ");
    Serial.print(indexThree);
    digitalWrite(indexThreePin,indexThree);
    Serial.print(indexTwo);
    digitalWrite(indexTwoPin,indexTwo);
    Serial.print(indexOne);
    digitalWrite(indexOnePin,indexOne);
    Serial.print(indexZero);
    digitalWrite(indexZeroPin,indexZero);
    Serial.println(" ]");
    Serial.println("--------------------");
    n=n+1;
    delay(1000);
  if(n>15){
    n=0;
  } 
   
}
