/*     Simple Stepper Motor Control Exaple Code
 *      
 *  by Dejan Nedelkovski, www.HowToMechatronics.com
 *  
 */
// defines pins numbers
const int stepPin = 10; 
const int dirPin = 9;
int customDelayMapped;
 
void setup() {
  // Sets the two pins as Outputs
  pinMode(stepPin,OUTPUT); 
  pinMode(dirPin,OUTPUT);
  customDelayMapped=450;
  digitalWrite(dirPin,LOW);
}
void loop() {
 digitalWrite(dirPin,LOW);
  for(int i=0; i<800; i++){
     digitalWrite(stepPin, HIGH);
  delayMicroseconds(customDelayMapped);
  digitalWrite(stepPin, LOW);
  delayMicroseconds(customDelayMapped);
  }
  digitalWrite(dirPin,HIGH);
   for(int i=0; i<800; i++){
     digitalWrite(stepPin, HIGH);
     delayMicroseconds(customDelayMapped);
  digitalWrite(stepPin, LOW);
  delayMicroseconds(customDelayMapped);
  }

}
