#include <Arduino.h>

extern "C" uint8_t secure_transform(uint8_t data, uint8_t key);

void setup() {
    Serial.begin(115200);
    DDRB |= (1 << DDB4); 
}

void loop() {
    if (Serial.available() > 0) {
        uint8_t challenge = (uint8_t)Serial.read();
        uint8_t response = secure_transform(challenge, 0x7A);
        Serial.write(response);
        
        PORTB |= (1 << PORTB4);
        delayMicroseconds(500);
        PORTB &= ~(1 << PORTB4);
    }
}