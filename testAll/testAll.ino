
int posX = 0;
int posY = 0;
const int stepPin = 10;
const int dirPinX = 9;


const int stepPinYLeft = 6;
const int dirPinYLeft = 5;

const int stepPinYRight = 3;
const int dirPinYRight = 2;

int stepsSetpointX;
int stepsSetpointY;
// Vi borde ha båda stepPinY till samma pin
int customDelayMapped;

void setup() {
  Serial.begin(9600);
  pinMode(stepPin, OUTPUT);
  pinMode(dirPinX, OUTPUT);

  pinMode(stepPinYRight, OUTPUT);
  pinMode(dirPinYRight, OUTPUT);

  pinMode(stepPinYLeft, OUTPUT);
  pinMode(dirPinYLeft, OUTPUT);
  customDelayMapped = 600;
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readString();
    String data1 = getValue(data, ':', 0);
    String data2 = getValue(data, ':', 1);
    Serial.println("data1: " + data1);
    Serial.println("data2: " + data2);
    int setpointX = data1.toInt();
    int setpointY = data2.toInt();
    stepsSetpointY = fromPixelsToSteps(setpointY);
    stepsSetpointX = fromPixelsToSteps(setpointX);
  }


  if (posX > 8000 ) {
    stepsSetpointX = 8000;
  }
  else if (posX < 0) {
    stepsSetpointX = 0;
  }
  if (posX != stepsSetpointX) {
    moveX(stepsSetpointX - posX);
  }

  
  if (posY > 4000) {
    stepsSetpointY = 4000;
  }
  else if (posY < 0) {
    stepsSetpointY = 0;
  }
  if (posY != stepsSetpointY) {
    moveY(stepsSetpointY - posY);
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
      strIndex[1] = (i == maxIndex) ? i + 1 : i;
    }
  }
  return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
}

void moveX(int errorX) {
  
  if (errorX > 0) {
    digitalWrite(dirPinX, LOW);
    posX = posX + 2;
  }
  else {
    digitalWrite(dirPinX, HIGH);
    posX = posX - 2;
  }
  digitalWrite(stepPin, HIGH);
  delayMicroseconds(customDelayMapped);
  digitalWrite(stepPin, LOW);
  delayMicroseconds(customDelayMapped);
}


void moveY(int errorY) {
  
  if (errorY > 0) {
    digitalWrite(dirPinYLeft, HIGH);
    digitalWrite(dirPinYRight, LOW);
    posY = posY + 2;
    
  }
  else {
    digitalWrite(dirPinYLeft, LOW);
    digitalWrite(dirPinYRight, HIGH);
    posY = posY-2;
  }
  digitalWrite(stepPinYLeft, HIGH);
  digitalWrite(stepPinYRight, HIGH);
  delayMicroseconds(customDelayMapped);
  digitalWrite(stepPinYLeft, LOW);
  digitalWrite(stepPinYRight, LOW);
  delayMicroseconds(customDelayMapped);
}

int fromPixelsToSteps(int val) {
  int converter = 1;
  return val / converter;
}

