const int led_blue = 9;
const int led_green = 7;
int led1Pin = led_blue; // pin number of LED output
const int sensorPin = 0; // pin number for sensing potentiometer
int brightness = 0; // variable for indicating how bright the LED is
int percent = 0;
int prevPercent = 0;
bool on = true;

void setup() {
  pinMode(led1Pin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int sensorValue;
  char buf[64];
  if(on){
    sensorValue = analogRead(sensorPin);
    percent = round( ( sensorValue / 1024.0 ) * 100);
    brightness = map(sensorValue, 0, 1023, 0, 255);
    if(sensorValue >= 0){
      analogWrite(led1Pin, brightness);
    }else{
      digitalWrite(led1Pin, LOW);
    }
  }else{
    digitalWrite(led1Pin, LOW);
  }
  //// serial information ....
  if(percent != prevPercent){
    //Serial.println(percent);
    prevPercent = percent;
  }
  if(Serial.available() > 0){
    String strCommand = String("ON");
    char msg[32];
    unsigned int pos = 0;
    while(Serial.available() > 0 && pos < 31){
      char inByte = Serial.read();
      msg[pos] = inByte;
      pos++;
    }
    msg[pos] = '\0';
    strCommand = String(msg);
    if( strCommand == "ON"){
      on = true;
      sprintf(buf, "msg: %s -> len %d (on)\n", msg, pos + 1);
    }else{
      if( strCommand == "OFF" ){
        on = false;
        sprintf(buf, "msg: %s -> len %d (off)\n", msg, pos + 1);
      }else{
        if( strCommand == "GREEN" ){
          led1Pin = led_green;
          digitalWrite(led_blue, LOW);
          sprintf(buf, "msg: %s -> len %d (green)\n", msg, pos + 1);
        }else{
          if( strCommand == "BLUE" ){
            led1Pin = led_blue;
            digitalWrite(led_green, LOW);
            sprintf(buf, "msg: %s -> len %d (blue)\n", msg, pos + 1);
          }else{
            sprintf(buf, "msg: %s -> len %d ()\n", msg, pos + 1);
          }
        }
      }
      
    }
    
    Serial.println(buf);
  }
  delay(100);
}
