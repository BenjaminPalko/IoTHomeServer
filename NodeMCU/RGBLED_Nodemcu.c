
/***************************************************
  NodeMCU
****************************************************/
#include <ESP8266WiFi.h>
#include "Adafruit_MQTT.h"
#include "Adafruit_MQTT_Client.h"
#include <ArduinoJson.h>
/************************* WiFi Access Point *********************************/
#define WLAN_SSID       "IoT-PROJECT-Wireless" 
#define WLAN_PASS       "JerryBetaLocal13" 
#define MQTT_SERVER     "192.168.1.3"  // give static address
#define MQTT_PORT       1883
#define MQTT_USERNAME   ""
#define MQTT_PASSWORD   ""
#define RED 5                    //pin connected to GPIO4 used to control the Red led
#define GREEN 4                  //pin connected to GPIO4 used to control the Green led
#define BLUE 0                   //pin connected to GPIO4 used to control the Blue led
#define RGBRATIO 4               //ratio between 10bit and 8bit value, as NodeMCU has 10bit pwm 
/************ Global State ******************/
// Create an ESP8266 WiFiClient class to connect to the MQTT server.
WiFiClient client;
// Setup the MQTT client class by passing in the WiFi client and MQTT server and login details.
Adafruit_MQTT_Client mqtt_client(&client, MQTT_SERVER, MQTT_PORT, MQTT_USERNAME, MQTT_PASSWORD);
/****************************** Feeds ***************************************/
// Setup a feed called 'esp8266_rgbled' for subscribing to changes.
Adafruit_MQTT_Subscribe nodemcu_rgbled = Adafruit_MQTT_Subscribe(&mqtt_client, MQTT_USERNAME "nodemcu/rgbled");
/*************************** Sketch Code ************************************/
void MQTT_connect();
void setup() {
  Serial.begin(115200);

  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);

  delay(10);
  Serial.println(F("NODEMCU-MQTT-RGBLED"));
  // Connect to WiFi access point.
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
  // Setup MQTT subscription for nodemcu_rgbled feed.
  mqtt_client.subscribe(&nodemcu_rgbled); 
  
}
uint32_t x = 0;

void loop() {
  
  // Ensure the connection to the MQTT server is alive (this will make the first
  // connection and automatically reconnect when disconnected).  See the MQTT_connect
  
  MQTT_connect();
  
  //char jsonmsg[] = "{\"Red\":0,\"Green\":255,\"Blue\":0}"; 

  DynamicJsonBuffer jsonBuffer;
  Adafruit_MQTT_Subscribe *subscription;

  while ((subscription = mqtt_client.readSubscription())) {

    if (subscription == &nodemcu_rgbled) {
      char *jsonmsg = (char *)nodemcu_rgbled.lastread;
      Serial.print(F("Got JSON: "));
      Serial.println(jsonmsg);

      JsonObject& msgpayload = jsonBuffer.parseObject((const char*)jsonmsg);
      if (!msgpayload.success()) {
        Serial.println("parseObject() failed");
      }
      else {
        int red = msgpayload["Red"];
        int green = msgpayload["Green"];
        int blue = msgpayload["Blue"];
        //change colour of RGBled
        analogWrite(RED, red * RGBRATIO);
        analogWrite(GREEN, green * RGBRATIO);
        analogWrite(BLUE, blue * RGBRATIO);
      }
    }
  }
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
