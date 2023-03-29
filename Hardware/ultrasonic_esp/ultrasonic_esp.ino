//Including the libraries
#if defined(ESP32)
  #include <WiFi.h>
#elif defined(ESP8266)
  #include <ESP8266WiFi.h>
#endif
#define trigPin D4 
#define echoPin D5 

long duration, inches, cm;
int distance1, distance2, measured_speed;
//#define CAYENNE_DEBUG
#define CAYENNE_PRINT Serial  // Comment this out to disable prints and save space
#include <CayenneMQTTESP8266.h>
// Insert your network credentials
#define WIFI_SSID "Omansh"
#define WIFI_PASSWORD "PCM12345"
// Initialize WiFi
// Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
char username[] = "e61d7e00-5958-11ed-bf0a-bb4ba43bd3f6";
char password[] = "b23fb2d033e81e6090bbdff16a51f369b3a33cae";
char clientID[] = "2f3e4a30-cda6-11ed-b0e7-e768b61d6137";

#define Measured_Speed 0
#define Distance 1 

void setup() {
Serial.begin(9600);      
initWiFi();
Cayenne.begin(username, password, clientID);
pinMode(trigPin, OUTPUT);
pinMode(echoPin, INPUT);  
}

void loop() {
Cayenne.loop();
}
int distance(){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  pinMode(echoPin, INPUT);
  duration = pulseIn(echoPin, HIGH);
  inches = microsecondsToInches(duration);
  cm = microsecondsToCentimeters(duration);
return cm;   
  }
void Speed(){
  distance1=distance();
  delay(1000);
  distance2=distance();
  measured_speed=abs(distance2-distance1);
  }
long microsecondsToInches(long microseconds)
{
 return microseconds / 74 / 2;
}

long microsecondsToCentimeters(long microseconds)
{
   return microseconds / 29 / 2;
}

void initWiFi() {
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to WiFi ..");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print('.');
    delay(1000);
  }
  Serial.println(WiFi.localIP());
  WiFi.setAutoReconnect(true);
  Serial.println();
}
CAYENNE_OUT(Measured_Speed)
{ 
  Speed();     
  Cayenne.virtualWrite(Measured_Speed, measured_speed);
  CAYENNE_LOG("Channel %d, value %d", Measured_Speed, measured_speed);
  delay(100);
}
CAYENNE_OUT(Distance)
{ distance();
  Cayenne.virtualWrite(Distance, cm);
  CAYENNE_LOG("Channel %d, value %d", Distance, cm);
  delay(100);
}
