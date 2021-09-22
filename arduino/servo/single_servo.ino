#include <Servo.h>

Servo servo1;  // creates servo 1

void setup() {
 Serial.begin(115200);
 servo1.attach(10);
}
void loop() {
    while (true) {
        int x = Serial.readString().toInt();

        servo1.write(0);
        delay(1000);
        servo1.write(x);
        delay(1000);
    }
}