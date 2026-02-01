#include <Arduino.h>

extern "C" uint8_t secure_transform(uint8_t data, uint8_t key);

void setup() {
    Serial.begin(115200);
    pinMode(12, OUTPUT);
}

void loop() {
    if (Serial.available() > 0) {
        uint8_t challenge = Serial.read();
        uint8_t response = secure_transform(challenge, 0x7A);
        Serial.write(response);
        digitalWrite(12, HIGH);
        delay(100);
        digitalWrite(12, LOW);
    }
}