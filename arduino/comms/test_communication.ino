int state = 0;
#define TYPE_INDEX 0
#define DATA_INDEX 1



void setup() {
 Serial.begin(115200);
 Serial.flush();

}

void loop() {
    char messageType;
    String data;
    if (!Serial.available()){
        String message = Serial.readStringUntil('\n');
        messageType = message.charAt(TYPE_INDEX);
        data = message.substring(DATA_INDEX);
    }
}
