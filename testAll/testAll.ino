
int posX=0;
int posY = 0;
const int stepPin = 10; 
const int dirPinX = 9;
const int dirPinYLeft = 5;
const int stepPinYLeft = 6;
const int dirPinYRight = 2;
const int stepPinYRight = 3;
// Vi borde ha båda stepPinY till samma pin
int customDelayMapped;

void setup() {
  Serial.begin(9600);
  pinMode(stepPin,OUTPUT); 
  pinMode(dirPinX,OUTPUT);
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
    int errorY = stepsSetpointY-posY;
    Serial.print("oldPosX: ");
    Serial.println(posX);
     //Serial.println(errorX+posX);
    if(errorX+posX>8000){
      moveX(8000-posX);
      Serial.println("Max");
    }
    else if(errorX+posX<0){
      moveX(-posX);
      Serial.println("Max");
    }
    else{
      moveX(errorX);
    }
    Serial.print("newPosX: ");
    Serial.println(posX);
    
    
    Serial.print("oldPosY: ");
    Serial.println(posY);
     //Serial.println(errorX+posX);
    if(errorY+posY>8000){
      moveX(8000-posY);
      Serial.println("Max");
    }
    else if(errorY+posY<0){
      moveX(-posY);
      Serial.println("Max");
    }
    else{
      moveX(errorY);
    }
    Serial.print("newPosY: ");
    Serial.println(posY);
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

void moveX(int errorX){
  if(errorX>0){
    digitalWrite(dirPinX,LOW);
  }
  else{
    digitalWrite(dirPinX, HIGH);
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

