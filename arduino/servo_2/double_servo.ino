#include <Servo.h>

Servo servo1;  // creates servo 1
Servo servo2;  // creates servo 2 
int wait_time = 0;

void setup() {
 Serial.begin(115200);
 servo1.attach(10);
 servo2.attach(9);
 
}
void loop() {


    while (true) {

        String x&y = Serial.readString();
        Serial.print(x&y);
        //int x = Serial.readString().toInt();
        
        //for(wait_time = 0; wait_time <= 100; wait_time += 1){
            //servo1.write(x);
            //servo2.write(x);
            //delay(15);
        //}

        
    }
}