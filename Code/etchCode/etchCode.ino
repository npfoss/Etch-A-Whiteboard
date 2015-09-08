#include <Stepper.h>
int pin1 = 10;
int pin2 = 11;
int pin3 = 12;
int pin4 = 13;
int enable = 9;
#define STEPS 50
Stepper cw(STEPS, pin3, pin4, pin1, pin2);
Stepper ccw(STEPS, pin1, pin2, pin3, pin4);

void setup(){
 Serial.begin(9600);
 cw.setSpeed(30);
 ccw.setSpeed(30);
 pinMode(enable, OUTPUT);
 digitalWrite(enable, HIGH);
 }

void loop(){
 int analogValue = analogRead(A0);
 Serial.println(analogValue);
 if(analogValue > 700)
 cw.step(STEPS);
 else if(analogValue < 300)
 ccw.step(STEPS);
 delay(100);
}
