
void setup() {
  Serial.begin(9600);
}
void loop() {
  if(Serial.available() > 0) {
    char Pos = Serial.read();
    String PosString  = Pos;
    String xPos;
    String yPos;
    boolean addToY=false;
    
    for(int i; i<PosString.size(); i++){
      if(PosString[i]==','){
        addToY=true;
      }
      if(addToy=false){
      xPos.append(PosString[i]);
      }
      else{
      yPos.append(PosString[i]);
      }
    }
    Serial.println(xPos);
    Serial.println(yPos);
  }
}
