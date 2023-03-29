#include <LiquidCrystal.h>    
const int rs = 10, en = 2, d4 = 6, d5 = 3, d6 = 4, d7 = 5;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

const int trigPin = 9; 
const int echoPin = 8; 
int red = 12;
int yellow = 13;
int buzzer =  7;
long duration, inches, cm; 
void setup() 
{
Serial.begin(9600);                                                   
pinMode(trigPin, OUTPUT);
pinMode(echoPin, INPUT);
pinMode(red, OUTPUT);
pinMode(yellow, OUTPUT);
pinMode(buzzer, OUTPUT);
delay(1000);
lcd.begin(16,2);
}

void loop(){
distance();
lights();                
Serial.println("");
delay(10);
Serial.print("Distance(cm):");
lcd.home();
lcd.print("Distance(cm): ");
lcd.setCursor(0,1);
lcd.print(cm);
delay(1000);
lcd.clear();
Serial.print(cm);
Serial.println("");
delay(1000);
}

void distance(){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  pinMode(echoPin, INPUT);
  duration = pulseIn(echoPin, HIGH);
  inches = microsecondsToInches(duration);
  cm = microsecondsToCentimeters(duration); 
  }
long microsecondsToInches(long microseconds)
{
 return microseconds / 74 / 2;
}

long microsecondsToCentimeters(long microseconds)
{
   return microseconds / 29 / 2;
}

void lights(){
  if (cm<40){
    digitalWrite(red,HIGH);
    digitalWrite(yellow,LOW);
    digitalWrite(buzzer,HIGH);
    }
  else{
    digitalWrite(yellow,HIGH);
    digitalWrite(red,LOW);
    delay(1000);
    digitalWrite(yellow,LOW);
    digitalWrite(buzzer,LOW);
    }
  }
