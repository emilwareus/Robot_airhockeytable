
int posX = 0;           //init starting positions 
int posY = 0;


const int stepPinX = 4; 
const int dirPinX = 2;


const int stepPinYLeft = 9;
const int dirPinYLeft = 7;

const int stepPinYRight = 13;
const int dirPinYRight = 11;

int stepsSetpointX;
int stepsSetpointY;
// Vi borde ha båda stepPinY till samma pin
int customDelayMapped;

int maxX = 7000;
int minX = 0;

int maxY = 3000;
int minY = 0;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);
  pinMode(stepPinX, OUTPUT);
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
  if (errorX != 0) {
    X = true;
    if (errorX > 0){
      digitalWrite(dirPinX, LOW);
      posX += 2;
    } 
    else {
      digitalWrite(dirPinX, HIGH);
      posX -= 2;
    }
  }
  //-------------------------------------------
  if (errorY != 0) {
    Y = true;
    if (errorY > 0) {
      digitalWrite(dirPinYLeft, HIGH);
      digitalWrite(dirPinYRight, LOW);
      posY += 2;
    } 
    else {
      digitalWrite(dirPinYLeft, LOW);
      digitalWrite(dirPinYRight, HIGH);
      posY -= 2;
    }
  }
  if (X) {
    digitalWrite(stepPinX, HIGH);
  }
  if (Y) {
    digitalWrite(stepPinYLeft, HIGH);
    digitalWrite(stepPinYRight, HIGH);
  }
  if(X || Y)delayMicroseconds(customDelayMapped);
  if (X) {
    digitalWrite(stepPinX, LOW);
  }
  if (Y) {
    digitalWrite(stepPinYLeft, LOW);
    digitalWrite(stepPinYRight, LOW);
  }
  if(X || Y)delayMicroseconds(customDelayMapped);
}


int fromPixelsToSteps(int val) {
  int converter = 1;
  return val / converter;
}


