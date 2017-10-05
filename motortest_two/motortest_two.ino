// defines pins numbers
const int stepPin = 10; 
const int dirPin = 9;
const int stepPin2 = 6; 
const int dirPin2 = 5;

int customDelayMapped;
 
void setup() {
  // Sets the two pins as Outputs
  pinMode(stepPin,OUTPUT); 
  pinMode(dirPin,OUTPUT);
  customDelayMapped=550;
  digitalWrite(dirPin,LOW);
  pinMode(stepPin2,OUTPUT); 
  pinMode(dirPin2,OUTPUT);
}
void loop() {
 digitalWrite(dirPin,LOW);
 digitalWrite(dirPin2,HIGH);
 
  for(int i=0; i<700; i++){
     digitalWrite(stepPin, HIGH);
     digitalWrite(stepPin2, HIGH);
  delayMicroseconds(customDelayMapped);
  digitalWrite(stepPin, LOW);
  digitalWrite(stepPin2, LOW);
  delayMicroseconds(customDelayMapped);
  }
  
  digitalWrite(dirPin,HIGH);
  digitalWrite(dirPin2,LOW);
  
   for(int i=0; i<700; i++){
     digitalWrite(stepPin, HIGH);
     digitalWrite(stepPin2, HIGH);
     delayMicroseconds(customDelayMapped);
  digitalWrite(stepPin, LOW);
  digitalWrite(stepPin2, LOW);
  delayMicroseconds(customDelayMapped);
  }
}
