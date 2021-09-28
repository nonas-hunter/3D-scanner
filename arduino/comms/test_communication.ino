int state = 0;
#define TYPE_INDEX 0
#define DATA_INDEX 1
#include <Servo.h>

void sendMessage(char messageType, String messageData) {
    Serial.print(messageType);
    Serial.println(messageData);
}

void analyzeMessage(String message) {
    char messageType = message.charAt(TYPE_INDEX);
    String data = message.substring(DATA_INDEX);
    switch (messageType) {
        case 'M':
            sendMessage('R', "MOTOR");
            break;
        case 'S':
            sendMessage('R', "SENSOR");
            break;
        case 'T':
            sendMessage('T', "12345");
            break;
    }
}

void setup() {
    Serial.begin(115200);
    Serial.flush();
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, LOW);
}

void loop() {
    if (Serial.available() > 0) {
        digitalWrite(LED_BUILTIN, HIGH);
        String message = Serial.readStringUntil('\n');
    } else {
        digitalWrite(LED_BUILTIN, LOW);
    }
}
