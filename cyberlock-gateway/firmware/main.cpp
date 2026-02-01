#include <Arduino.h>
extern "C" uint8_t fast_verify(uint8_t d, uint8_t k);

void setup() {
    Serial.begin(115200);
    pinMode(13, OUTPUT); 
}

void loop() {
    if(Serial.available()) {
        uint8_t key = 0xAB;
        uint8_t input = Serial.read();
        if(fast_verify(input, key) == 0x54) { 
            digitalWrite(13, HIGH); 
        }
    }
}