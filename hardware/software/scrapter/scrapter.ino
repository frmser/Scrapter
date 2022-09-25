// scrapter

#include "WiFi.h"
#include <WebServer.h>

WebServer server(80);

int time_up = 1080; // The higher the number, the slower the timing. In Milliseconds
int time_down = 1070;
int time_rightleft = 5050;

int pin_right = 32;
int pin_left = 33;
int pin_up = 26;
int pin_down = 25;

//move robot arm to the right
void move_right () {
  digitalWrite(pin_up, LOW);
  digitalWrite(pin_down, LOW);
  digitalWrite(pin_left, LOW);


  digitalWrite(pin_right, HIGH);
  long timer = millis();
  while((millis() - timer) <= time_rightleft) {
    yield();
  }
  digitalWrite(pin_right, LOW);
}

void move_left () {
  digitalWrite(pin_up, LOW);
  digitalWrite(pin_down, LOW);
  digitalWrite(pin_right, LOW);


  digitalWrite(pin_left, HIGH);
  long timer = millis();
  while((millis() - timer) <= time_rightleft) {
    yield();
  }
  digitalWrite(pin_left, LOW);
}

void move_up () {
  digitalWrite(pin_down, LOW);
  digitalWrite(pin_left, LOW);
  digitalWrite(pin_right, LOW);

  digitalWrite(pin_up, HIGH);
  long timer = millis();
  while((millis() - timer) <= time_up) {
    yield();
  }
  digitalWrite(pin_up, LOW);
}

void move_down () {
  digitalWrite(pin_up, LOW);
  digitalWrite(pin_left, LOW);
  digitalWrite(pin_right, LOW);

  digitalWrite(pin_down, HIGH);
  long timer = millis();
  while((millis() - timer) <= time_down) {
    yield();
  }
  digitalWrite(pin_down, LOW);
}

void setup() {
  pinMode(pin_up, OUTPUT);
  digitalWrite(pin_up, LOW);
  pinMode(pin_down, OUTPUT);
  digitalWrite(pin_down, LOW);
  pinMode(pin_left, OUTPUT);
  digitalWrite(pin_left, LOW);
  pinMode(pin_right, OUTPUT);
  digitalWrite(pin_right, LOW);
  
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.begin("UNI-LAPTOP 1298", "h5O445#5");
  Serial.print("Connecting to WiFi ..");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print('.');
    delay(1000);
  }
  Serial.println(WiFi.localIP());
  server.on("/up", handle_up);
  server.on("/down", handle_down);
  server.on("/left", handle_left);
  server.on("/right", handle_right);
  server.begin();
}

void loop() {
  server.handleClient();
}

void handle_up() {
  Serial.println("Received up");
  move_up();
  server.send(200, "text/html", "ok");
}

void handle_down() {
  Serial.println("Received down");
  move_down();
  server.send(200, "text/html", "ok");
}

void handle_left() {
  Serial.println("Received left");
  move_left();
  server.send(200, "text/html", "ok");
}

void handle_right() {
  Serial.println("Received right");
  move_right();
  server.send(200, "text/html", "ok");
}