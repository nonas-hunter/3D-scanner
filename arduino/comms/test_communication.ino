int state = 0;
#define TYPE_INDEX 0
#define DATA_INDEX 1
#define M1 1
#define M2 4
#define MEND 8
#include <Servo.h>

//sensor
int distancesensor = 0;
int value = 0;

Servo servo1;  // creates servo 1
Servo servo2;  // creates servo 2 
int wait_time = 0;

void sayHi() {
    Serial.print("yo.");
}

void setup() {
 Serial.begin(115200);
 Serial.flush();
 servo1.attach(10);
 servo2.attach(9);
}

void loop() {
    char messageType;
    String data;
    if (!Serial.available()){
        String message = Serial.readStringUntil('\n');
        messageType = message.charAt(TYPE_INDEX);
        data = message.substring(DATA_INDEX);
    }
            
            
    switch (messageType) {
        case 'M': {
            
            int M1Pos = data.substring(M1, M2).toInt();
            int M2Pos = data.substring(M2, MEND).toInt();
            
            
            servo1.write(M1Pos);
            servo2.write(M2Pos);
            //Serial.print(M1Pos);
            //Serial.print("+");
            //Serial.println(M2Pos);
            delay(1000);
            value = analogRead(distancesensor);
            Serial.print('R');
            Serial.print(M1Pos);
            Serial.print(",");
            Serial.print(M2Pos);
            Serial.print(",");
            Serial.println(value);
        }
            break;
        case 'S':
            {
            //value = analogRead(distancesensor);
            Serial.print('R');
            Serial.println("HELLo");
            }
            break;
        default:
            {
            Serial.print('R');
            Serial.println(messageType);
            }
            break;
    }
}
