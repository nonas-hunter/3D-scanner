#include <Servo.h>
int pos1 = 0;
int pos2 = 0;

Servo servo1;  // creates servo 1
Servo servo2;  // creates servo 2

int x;
void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
 servo1.attach(9);
 servo2.attach(10);
}
void loop() {
 while (!Serial.available());
 int x = Serial.readString().toInt();
 int y = Serial.readString().toInt();
 
 for (pos1 = 0; pos1 <= x; pos1 += 1){\
    servo1.write(pos1);
    delay(15);
 }

 for (pos2 = 0; pos2 <= y; pos1 += 1){\
    servo2.write(pos2);
    delay(15);
 }
 
 Serial.print(true);
}