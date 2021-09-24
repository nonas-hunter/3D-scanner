#include <Servo.h>

Servo servo1;  // creates servo 1
Servo servo2;  // creates servo 2 

void setup() {
 Serial.begin(115200);
 servo1.attach(10);
 servo2.attach(9);
}
void loop() {
    while (true) {
        int x = Serial.readString().toInt();
        int y = Serial.readString().toInt();

        servo1.write(0);
        servo2.write(0);
        delay(1000);
        servo1.write(x);
        servo2.write(y);
        delay(1000);

        Serial.print(true);
    }
}