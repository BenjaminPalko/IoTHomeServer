/***************************************************
  NodeMCU
****************************************************/
#include <ESP8266WiFi.h>
#include "Adafruit_MQTT.h"
#include "Adafruit_MQTT_Client.h"
#include <ArduinoJson.h>
#include <Servo.h>
/************************* WiFi Access Point *********************************/
#define WLAN_SSID       "BELL957" 
#define WLAN_PASS       "1746FA2C4263" 
#define MQTT_SERVER     "3.84.42.130"  // give static address
#define MQTT_PORT       1883
#define MQTT_USERNAME   ""
#define MQTT_PASSWORD   ""
#define DOORLOCK_SUB "nodemcu/doorlock/sub"
#define DOORLOCK_PUB "nodemcu/doorlock/pub"
/************ Global State ******************/
// Create an ESP8266 WiFiClient class to connect to the MQTT server.
WiFiClient client;
// Setup the MQTT client class by passing in the WiFi client and MQTT server and login details.
Adafruit_MQTT_Client mqtt_client(&client, MQTT_SERVER, MQTT_PORT, MQTT_USERNAME, MQTT_PASSWORD);

const int lockButton = 4;
const int keyButton1 = 12;
const int keyButton2 = 13;
const int keyButton3 = 14;
const int servoPin = 15;
int lockButtonRead = 0, keyButton1Read = 0, keyButton2Read = 0, keyButton3Read = 0;
int passcode_counter = 0;

String passcode;
Servo servo;
/****************************** Feeds ***************************************/
// Setup a feed called 'esp8266_rgbled' for subscribing to changes.

Adafruit_MQTT_Subscribe nodemcu_doorlock_sub = Adafruit_MQTT_Subscribe(&mqtt_client,DOORLOCK_SUB);


void setup() {
  //set the buttons as INPUT_PULLUP and initialize the servo
  Serial.begin(115200);
  pinMode(lockButton,INPUT_PULLUP);
  pinMode(keyButton1,INPUT_PULLUP);
  pinMode(keyButton2,INPUT_PULLUP);
  pinMode(keyButton3,INPUT_PULLUP);
  servo.attach(servoPin);
  servo.write(0);
  
  delay(10);
  Serial.println(F("NODEMCU-MQTT-DOORLOCK"));
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
  mqtt_client.subscribe(&nodemcu_doorlock_sub); 
}

void loop() {
  // Ensure the connection to the MQTT server is alive (this will make the first
  // connection and automatically reconnect when disconnected). 
  MQTT_connect();

  DynamicJsonBuffer jsonBuffer;
  Adafruit_MQTT_Subscribe *subscription;

  //check for any incoming messages from the server for validation
  while ((subscription = mqtt_client.readSubscription())) {
    if (subscription == &nodemcu_doorlock_sub) {
      char *jsonmsg = (char *)nodemcu_doorlock_sub.lastread;
      Serial.print(F("Got JSON: "));
      Serial.println(jsonmsg);

      JsonObject& msgpayload = jsonBuffer.parseObject((const char*)jsonmsg);
      if (!msgpayload.success()) {
        Serial.println("parseObject() failed");
      }
      else {
        int validation = msgpayload["validation"];
        if(validation == 1){
          Serial.println("Validation Sucess, Unlocking Door");
          servo.write(180);
        }
        else{
          Serial.println("Validation Failed, Incorrected passcode");
        }
      }
    }
  }
  //read the signals for all the buttons
  lockButtonRead = digitalRead(lockButton);
  keyButton1Read = digitalRead(keyButton1);
  keyButton2Read = digitalRead(keyButton2);
  keyButton3Read = digitalRead(keyButton3);
  
  //if lock button was pressed, close the servo and reset the passcode and passcode counter.
  //if a key button was pressed, add the corresponding value to the passcode. Send the passcode when it's 4 digits long
  if(lockButtonRead == HIGH){
    Serial.println("Lock Button Pressed");
    servo.write(0);
    passcode = "";
    passcode_counter = 0;
    delay(250);
  }
  else if(keyButton1Read == HIGH){
    Serial.println("KeyButton1 pressed");
    passcode += 1;
    passcode_counter++;
    if(passcode_counter == 4){
      sendPasscode();
    }
    delay(250);
  }
  else if(keyButton2Read == HIGH){
    Serial.println("KeyButton2 pressed");
    passcode += 2;
    passcode_counter++;
    if(passcode_counter == 4){
      sendPasscode();
    }
    delay(250);
  }
  else if(keyButton3Read == HIGH){
    Serial.println("KeyButton3 pressed");
    passcode += 3;
    passcode_counter++;
    if(passcode_counter == 4){
      sendPasscode();
    }
    delay(250);
  }
}

//Method to publish the passcode to the server to verify the passcode input was correct
void sendPasscode(){
  //create and publish a JSON to the server containing the passcode
  DynamicJsonBuffer jsonBuffer; 
  JsonObject& root = jsonBuffer.createObject();
  char JSONmessageBuffer[20];
  root["passcode"] = passcode.toInt();
  root.printTo(JSONmessageBuffer,sizeof(JSONmessageBuffer));
  mqtt_client.publish(DOORLOCK_PUB,JSONmessageBuffer);
  //reset the passcode and passcode_counter for future attemps
  passcode = "";
  passcode_counter = 0;
}

// Method to connect and reconnect as necessary to the MQTT server.
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
  
