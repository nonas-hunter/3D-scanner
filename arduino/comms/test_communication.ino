#define TYPE_INDEX 0
#define DATA_INDEX 1
#define PITCH_SERVO_PIN 9
#define YAW_SERVO_PIN 10
#include <Servo.h>

Servo pitchServo;
Servo yawServo;

void sendMessage(char messageType, String messageData) {
    /* Send a message to python using serial
     * 
     * Parameters:
     *  messageType (char): the type of the message. Examples include, 'R' for
     *      response, 'T' for test.
     * messageData (String): the message data to be sent.
     */
    Serial.print(messageType);
    Serial.println(messageData);
}

void analyzeMessage(String message) {
    /* Decode serial messages from python and execute corresponding
     * response function.
     * 
     * Parameters:
     *  message (String): the raw message sent over serial from python.
     */
    char messageType = message.charAt(TYPE_INDEX);
    String data = message.substring(DATA_INDEX);
    switch (messageType) {
        case 'M':
            sendMessage('M', "");
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
    /* The setup function starts serial communcation, sets up a debug LED, and
     * assigns PWM pins to servos. 
     */
    Serial.begin(115200);
    Serial.flush();
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, LOW);

    pitchServo.attach(PITCH_SERVO_PIN);
    yawServo.attach(YAW_SERVO_PIN);
}

void loop() {
    /* The main loop reads incoming serial messages and sends them
     * to the analyzeMessage function where they are decoded and the
     * proper actions are taken.
     */
    if (Serial.available() > 0) {
        digitalWrite(LED_BUILTIN, HIGH);
        String message = Serial.readStringUntil('\n');
        analyzeMessage(message);
    } else {
        digitalWrite(LED_BUILTIN, LOW);
    }
}
