
int posX = 0;           //init starting positions 
int posY = 0;


const int stepPinY = 4; 
const int dirPinY = 2;


const int stepPinXLeft = 9;
const int dirPinXLeft = 7;

const int stepPinXRight = 13;
const int dirPinXRight = 11;

int stepsSetpointX;
int stepsSetpointY;
// Vi borde ha båda stepPinY till samma pin
int customDelayMapped;

int maxX = 1500;
int minX = 0;

int maxY = 3500;
int minY = 0;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);
  pinMode(stepPinY, OUTPUT);
  pinMode(dirPinY, OUTPUT);

  pinMode(stepPinXRight, OUTPUT);
  pinMode(dirPinXRight, OUTPUT);

  pinMode(stepPinXLeft, OUTPUT);
  pinMode(dirPinXLeft, OUTPUT);
  customDelayMapped = 600;
}




void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readString();
    String data1 = getValue(data, ':', 0);
    String data2 = getValue(data, ':', 1);
    //Serial.println("data1: " + data1);
    //Serial.println("data2: " + data2);
    int setpointX = data1.toInt();
    int setpointY = data2.toInt();
    stepsSetpointY = fromPixelsToSteps(setpointY);
    stepsSetpointX = fromPixelsToSteps(setpointX);
  }


  if (posX > maxX ) {
    stepsSetpointX = maxX;
     Serial.println(posX);
  }
  else if (posX < minX) {
    stepsSetpointX = minX;
    Serial.println(posX);
  }

  if (posY > maxY) {
    stepsSetpointY = maxY;
    Serial.println(posY);
  }
  else if (posY < minY) {
    stepsSetpointY = minY;
    Serial.println(posY);
  }

  MoveXY(stepsSetpointX - posX, stepsSetpointY - posY);  
  }


String getValue(String data, char separator, int index)
{
  int found = 0;
  int strIndex[] = { 
    0, -1   };
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

void MoveXY(int errorX, int errorY) {
  
    boolean X  = false;
    boolean Y = false;
  //--------------------------------------------------------
  if (errorY != 0) {
    Y = true;
    if (errorY > 0){
      digitalWrite(dirPinY, LOW);
      posY++;
    } 
    else {
      digitalWrite(dirPinY, HIGH);
      posY--;
    }
  }
  //-------------------------------------------
  if (errorX != 0) {
    X = true;
    if (errorX > 0) {
      digitalWrite(dirPinXLeft, HIGH);
      digitalWrite(dirPinXRight, LOW);
      posX++;
    } 
    else {
      digitalWrite(dirPinXLeft, LOW);
      digitalWrite(dirPinXRight, HIGH);
      posX--;
    }
  }
  if (Y) {
    digitalWrite(stepPinY, HIGH);
  }
  if (X) {
    digitalWrite(stepPinXLeft, HIGH);
    digitalWrite(stepPinXRight, HIGH);
  }
  if(X || Y)delayMicroseconds(customDelayMapped);
  if (Y) {
    digitalWrite(stepPinY, LOW);
  }
  if (X) {
    digitalWrite(stepPinXLeft, LOW);
    digitalWrite(stepPinXRight, LOW);
  }
  if(X || Y)delayMicroseconds(customDelayMapped);
}


int fromPixelsToSteps(int val) {
  int converter = 1;
  return val / converter;
}


