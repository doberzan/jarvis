
int led = 12;
int gun = 8;
int inByte = 0;
void setup() {           
  Serial.begin(9600);
  pinMode(led, OUTPUT); 
  pinMode(gun, OUTPUT);  
}

void loop() {
  if (Serial.available() > 0) {
    inByte = Serial.read() ;
    Serial.println(inByte);
    if (inByte == 104){
      digitalWrite(gun, HIGH);
      delay(800);
      digitalWrite(gun, LOW);
    }
    if (inByte == 'a'){
          digitalWrite(led, HIGH); 
    }
    if (inByte == 'b'){
          digitalWrite(led, LOW);   
    }
    if (inByte == '1'){
       int i = 0;
       while(i < 100){
          digitalWrite(led, HIGH);
          delay(50);
          digitalWrite(led, LOW); 
          delay(50);
          i++;
       }
    }
    if (inByte == 50){
      boolean run = true;
      while(run){
          int msg = Serial.read();
          if ( msg == '2'){
           run = false; 
          }
          delay(1000);
          digitalWrite(led, HIGH);
          delay(1000);
          digitalWrite(led, LOW);
      }
    }
  }  // wait for a second
}
