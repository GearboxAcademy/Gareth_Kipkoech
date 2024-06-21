int snakeLights[7]={15,2,0,4,16,17,5};
int pos=0;
int diff=1;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("Snake Lights on ESP32!");
  for(int i=0;i<7;i++){
    pinMode(snakeLights[i],OUTPUT);
    delay(10);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i=0;i<7;i++){
    if(i==pos){
      digitalWrite(snakeLights[i],HIGH);
      delay(200);
      digitalWrite(snakeLights[i],LOW);
    }
    pos+=diff;
    if(pos>=6 || pos<=0){
      diff*=-1;
    }
  }
}
