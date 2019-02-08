#include <ESP8266WiFi.h> 
#include "Adafruit_MQTT.h" 
#include "Adafruit_MQTT_Client.h" 
#include <ArduinoJson.h>

#define WLAN_SSID       "BELL957" 
#define WLAN_PASS       "1746FA2C4263" 
#define MQTT_SERVER     "3.84.42.130"  // give static address
#define MQTT_PORT        1883                    
#define MQTT_USERNAME    "" 
#define MQTT_PASSWORD    "" 
#define TEMP_PIN         A0 


//create ESP8266 WifiClient class
WiFiClient client; 
//initialize MQTT client using the WiFi client and the MQTT server IP address(RASPI)
Adafruit_MQTT_Client mqtt_client(&client, MQTT_SERVER, MQTT_PORT, MQTT_USERNAME, MQTT_PASSWORD);

//Setup a feed called "mcu_temp" for publishing temp data
//Adafruit_MQTT_Publish nodemcu_temp = Adafruit_MQTT_Publish(&mqtt_client, MQTT_USERNAME "nodemcu/temp");

void MQTT_connect();

void setup() {
  Serial.begin(115200);
  delay(10);
  
  //connect to WiFi
  Serial.print("Connecting to "); 
  Serial.println(WLAN_SSID); 
  WiFi.begin(WLAN_SSID, WLAN_PASS); 
  while (WiFi.status() != WL_CONNECTED) { 
   delay(500); 
   Serial.print("."); 
  } 
  Serial.println(); 
  Serial.println("WiFi connected"); 
  Serial.println("IP address: "); Serial.println(WiFi.localIP()); 
  

}
uint32_t x=0; 
void loop() {
  //connect to MQTT Server
  MQTT_connect();
  
  
  int sensorVal = analogRead(TEMP_PIN);
  Serial.print("Sensor Value: ");
  Serial.println(sensorVal);
  delay(500);

  float voltage = (sensorVal * 3.3) / 1024.0;
  Serial.print("Voltage: ");
  Serial.println(voltage);

  Serial.print("Temperature(C): ");
  float temp = (voltage - 0.5) * 100;
  Serial.println(temp);
  Serial.println();

  DynamicJsonBuffer jsonBuffer; 
  JsonObject& root = jsonBuffer.createObject();
  char JSONmessageBuffer[100];
  root["temperature"] = temp;
  root.printTo(JSONmessageBuffer,sizeof(JSONmessageBuffer));
  mqtt_client.publish("nodemcu/temp",JSONmessageBuffer);
  delay(5000);
}

// Function to connect and reconnect as necessary to the MQTT server. 
void MQTT_connect() { 
 int8_t ret; 
 // Stop if already connected. 
 if (mqtt_client.connected()) { 
   return; 
 } 
 Serial.print("Connecting to MQTT... "); 
 uint8_t retries = 3; 
 while ((ret = mqtt_client.connect()) != 0) { // connect will return 0 for connected 
      Serial.println(mqtt_client.connectErrorString(ret)); 
      Serial.println("Retrying MQTT connection in 5 seconds..."); 
      mqtt_client.disconnect(); 
      delay(5000);  // wait 5 seconds 
      retries--; 
      if (retries == 0) { 
        // basically die and wait for WDT to reset me 
        while (1); 
      } 
 } 
 Serial.println("MQTT Connected!"); 
} 
