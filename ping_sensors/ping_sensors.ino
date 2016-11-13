/*
 HC-SR04 Ping distance sensor:
 VCC to arduino 5v 
 GND to arduino GND
 Echo to Arduino pin 7 
 Trig to Arduino pin 8
 
 This sketch originates from Virtualmix: http://goo.gl/kJ8Gl
 Has been modified by Winkle ink here: http://winkleink.blogspot.com.au/2012/05/arduino-hc-sr04-ultrasonic-distance.html
 And modified further by ScottC here: http://arduinobasics.blogspot.com.au/2012/11/arduinobasics-hc-sr04-ultrasonic-sensor.html
 on 10 Nov 2012.
 */


#define echoPin_1 12 // Echo Pin
#define trigPin_1 11 // Trigger Pin
#define OpenPin_1 10 // Onboard LED
#define ClosedPin_1 9


#define echoPin_2 8 // Echo Pin
#define trigPin_2 7 // Trigger Pin
#define OpenPin_2 6 // Onboard LED
#define ClosedPin_2 5

#define echoPin_3 4 // Echo Pin
#define trigPin_3 3 // Trigger Pin
#define OpenPin_3 2 // Onboard LED
#define ClosedPin_3 13

int sensor = 1;
int maximumRange = 80; // Maximum range needed
int minimumRange = 0; // Minimum range needed
long duration_1,duration_2,duration_3, distance_1,distance_2,distance_3; // Duration used to calculate distance

unsigned long startTime;
unsigned long endTime;

int senseCount_1 = 0;
int senseCount_2 = 0;
int senseCount_3 = 0;

void setup() {
 Serial.begin (9600);
 pinMode(trigPin_1, OUTPUT);
 pinMode(echoPin_1, INPUT);
 pinMode(OpenPin_1, OUTPUT); // Use LED indicator (if required)
 pinMode(ClosedPin_1, OUTPUT);

 pinMode(trigPin_2, OUTPUT);
 pinMode(echoPin_2, INPUT);
 pinMode(OpenPin_2, OUTPUT); // Use LED indicator (if required)
 pinMode(ClosedPin_2, OUTPUT);

 pinMode(trigPin_3, OUTPUT);
 pinMode(echoPin_3, INPUT);
 pinMode(OpenPin_3, OUTPUT); // Use LED indicator (if required)
 pinMode(ClosedPin_3, OUTPUT);


 digitalWrite(OpenPin_1, LOW);
 digitalWrite(ClosedPin_1, HIGH); 
 digitalWrite(OpenPin_2, LOW);
 digitalWrite(ClosedPin_2, HIGH); 
 digitalWrite(OpenPin_3, LOW);
 digitalWrite(ClosedPin_3, HIGH); 
 startTime = millis();
}

void loop() {

  if(sensor==1){
    pingSensor_1();
  }else if(sensor==2){
    pingSensor_2();
  }
  
  //delay(150);
  
  if(sensor>=2){
    sensor = 1;  
  }else{
    sensor++;
  }

  endTime = millis();
  if((endTime-startTime)>= 100){
    if(senseCount_1 >= 1){
      digitalWrite(OpenPin_1, HIGH);
      digitalWrite(ClosedPin_1, LOW);
      Serial.println("-1"); 
    }else{
      digitalWrite(OpenPin_1, LOW);
      digitalWrite(ClosedPin_1, HIGH);
      Serial.println("1");
    }

    if(senseCount_2 >= 1){
      digitalWrite(OpenPin_2, HIGH);
      digitalWrite(ClosedPin_2, LOW); 
      Serial.println("-2");
    }else{
      digitalWrite(OpenPin_2, LOW);
      digitalWrite(ClosedPin_2, HIGH);
      Serial.println("2");
    }

    if(senseCount_3 >= 3){
      digitalWrite(OpenPin_3, HIGH);
      digitalWrite(ClosedPin_3, LOW);
      Serial.println("-3"); 
    }else{
      digitalWrite(OpenPin_3, LOW);
      digitalWrite(ClosedPin_3, HIGH);
      Serial.println("3");
    }

    senseCount_1 = 0;
    senseCount_2 = 0;
    

    startTime = millis();
  }
}

void pingSensor_1(){
  
 digitalWrite(trigPin_1, LOW);  
 delayMicroseconds(2); 

 digitalWrite(trigPin_1, HIGH);
 delayMicroseconds(10); 
 
 digitalWrite(trigPin_1, LOW);
 duration_1 = pulseIn(echoPin_1, HIGH);
 
 //Calculate the distance (in cm) based on the speed of sound.
 distance_1 = duration_1/58.2;
 
 if (distance_1 >= maximumRange || distance_1 <= minimumRange){
 /* Send a negative number to computer and Turn LED ON 
 to indicate "out of range" */
 //Serial.println("-1");
 senseCount_1 ++;
 //digitalWrite(OpenPin_1, HIGH); 
 //digitalWrite(ClosedPin_1,LOW);
 }
 else {
 /* Send the distance to the computer using Serial protocol, and
 turn LED OFF to indicate successful reading. */
 //Serial.println(distance);
 //Serial.println("1");
 //digitalWrite(OpenPin_1, LOW);
 //digitalWrite(ClosedPin_1, HIGH); 
 }


}

void pingSensor_2(){
  
 digitalWrite(trigPin_2, LOW);  
 delayMicroseconds(2); 

 digitalWrite(trigPin_2, HIGH);
 delayMicroseconds(10); 
 
 digitalWrite(trigPin_2, LOW);
 duration_2 = pulseIn(echoPin_2, HIGH);
 
 //Calculate the distance (in cm) based on the speed of sound.
 distance_2 = duration_2/58.2;
 
 if (distance_2 >= maximumRange || distance_2 <= minimumRange){
 /* Send a negative number to computer and Turn LED ON 
 to indicate "out of range" */
 //Serial.println("-2");
 senseCount_2 ++;
 //digitalWrite(OpenPin_2, HIGH); 
 //digitalWrite(ClosedPin_2,LOW);
 }
 else {
 /* Send the distance to the computer using Serial protocol, and
 turn LED OFF to indicate successful reading. */
 //Serial.println(distance);
 //Serial.println("2");
 //digitalWrite(OpenPin_2, LOW);
 //digitalWrite(ClosedPin_2, HIGH); 
 }


}

void pingSensor_3(){
  
 digitalWrite(trigPin_3, LOW);  
 delayMicroseconds(2); 

 digitalWrite(trigPin_3, HIGH);
 delayMicroseconds(10); 
 
 digitalWrite(trigPin_3, LOW);
 duration_3 = pulseIn(echoPin_3, HIGH);
 
 //Calculate the distance (in cm) based on the speed of sound.
 distance_3 = duration_3/58.2;
 
 if (distance_3 >= maximumRange || distance_3 <= minimumRange){
 /* Send a negative number to computer and Turn LED ON 
 to indicate "out of range" */
 //Serial.println("-3");
 senseCount_3++;
 //digitalWrite(OpenPin_3, HIGH); 
 //digitalWrite(ClosedPin_3,LOW);
 }
 else {
 /* Send the distance to the computer using Serial protocol, and
 turn LED OFF to indicate successful reading. */
 //Serial.println(distance);
 //Serial.println("3");
 //digitalWrite(OpenPin_3, LOW);
 //digitalWrite(ClosedPin_3, HIGH); 
 }


}
