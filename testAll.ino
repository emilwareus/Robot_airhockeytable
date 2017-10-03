
int posX=0;
const int stepPin = 10; 
const int dirPin = 9;
int customDelayMapped;
void setup() {
  Serial.begin(9600);
  pinMode(stepPin,OUTPUT); 
  pinMode(dirPin,OUTPUT);
  customDelayMapped=600;
}
void loop() {
  if(Serial.available() > 0) {
    String data = Serial.readString();
    String data1 = getValue(data, ':', 0);
    String data2 = getValue(data, ':', 1);
    Serial.println("data1: " + data1);
    Serial.println("data2: " + data2);
    int setpointX= data1.toInt();
    int setpointY =data2.toInt();
    int stepsSetpointY = fromPixelsToSteps(setpointY);
    int stepsSetpointX = fromPixelsToSteps(setpointX);
    int errorX = stepsSetpointX-posX;
    Serial.print("oldPosX: ");
     Serial.println(posX);
     Serial.println(errorX+posX);
    if(errorX+posX>8000){
      move(8000-posX);
      Serial.println("Max");
    }
    else if(errorX+posX<0){
    move(-posX);
    Serial.println("Max");
    }
    else{
    move(errorX);
    }
    Serial.print("newPosX: ");
    Serial.println(posX);
  }
}


String getValue(String data, char separator, int index)
{
    int found = 0;
    int strIndex[] = { 0, -1 };
    int maxIndex = data.length() - 1;

    for (int i = 0; i <= maxIndex && found <= index; i++) {
        if (data.charAt(i) == separator || i == maxIndex) {
            found++;
            strIndex[0] = strIndex[1] + 1;
            strIndex[1] = (i == maxIndex) ? i+1 : i;
        }
    }
    return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
}

void move(int errorX){
  if(errorX>0){
    digitalWrite(dirPin,LOW);
  }
  else{
    digitalWrite(dirPin, HIGH);
  }
  posX=posX+errorX;
  for( int i=0; i < abs(errorX/2); i++){
  digitalWrite(stepPin, HIGH);
  delayMicroseconds(customDelayMapped);
  digitalWrite(stepPin, LOW);
  delayMicroseconds(customDelayMapped);
  }
}

int fromPixelsToSteps(int val){
  int converter=1;
  return val/converter;
}

