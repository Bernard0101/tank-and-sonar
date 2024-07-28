#include <Servo.h>

Servo servo;
int trig=3;
int echo=4;
long duration;
int distance;

void setup(){
  Serial.begin(9600);

  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  servo.attach(2);
}
void loop(){
  for(int pos=0; pos<=180; pos++){
    servo.write(pos);

    digitalWrite(trig, LOW);
    delay(2);
    digitalWrite(trig, HIGH);
    delay(10);
    digitalWrite(trig, LOW);

    long startTime = micros();
    while (digitalRead(echo) == LOW);
    long echoStart = micros();
    while (digitalRead(echo) == HIGH);
    long echoEnd = micros();

    duration = echoEnd - echoStart;
    distance = duration * 0.034 / 2;

    Serial.print(pos);
    Serial.print(",");
    Serial.print(distance);
    Serial.println("");
  }
  for(int pos=180; pos>=0; pos--){
    servo.write(pos);

    digitalWrite(trig, LOW);
    delay(2);
    digitalWrite(trig, HIGH);
    delay(10);
    digitalWrite(trig, LOW);

    long startTime = micros();
    while (digitalRead(echo) == LOW);
    long echoStart = micros();
    while (digitalRead(echo) == HIGH);
    long echoEnd = micros();

    duration = echoEnd - echoStart;
    distance = duration * 0.034 / 2;

    Serial.print(pos);
    Serial.print(",");
    Serial.print(distance);
    Serial.println("");
  }
}