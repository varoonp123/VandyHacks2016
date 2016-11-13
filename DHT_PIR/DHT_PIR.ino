// Example testing sketch for various DHT humidity/temperature sensors
// Written by ladyada, public domain

#include "DHT.h"

#define DHTPIN 2     // what digital pin we're connected to
#define ledPin 4
#define PIRPin 3

#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321

DHT dht(DHTPIN, DHTTYPE);

String output;
int pirTime;

unsigned long startTime;

unsigned long pirStartTime;

int modifier;

int cycles = 0;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin,OUTPUT);
  pinMode(PIRPin,INPUT);
  dht.begin();

  pirTime = 0;
  startTime = 0;
  pirStartTime = 0;
  modifier = 0;
}

void loop() {
  
  
  readPir();
  delay(10);
  
  if((millis()-startTime) >= 8000){

    output = readTemp() +"-"+ (String)pirTime;

    
    Serial.println(output);
    
    pirTime = 0;
    startTime = millis();
  }
  
  
}

String readTemp(){
  
  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("-1");
    return;
  }

  float hif = dht.computeHeatIndex(f, h);
  String hifStr = (String)hif;
  return hifStr;
}

void readPir(){

  if(digitalRead(PIRPin)){
    pirStartTime = millis();
    digitalWrite(ledPin,HIGH);
    pirTime++;
  }else{
    digitalWrite(ledPin,LOW);  
  }

}
