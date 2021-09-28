#define TYPE_INDEX 0
#define DATA_INDEX 1
#define PITCH_SERVO_PIN 9
#define YAW_SERVO_PIN 10
#define DISTANCE_SENSOR_PIN 1
#include <Servo.h>

Servo pitchServo;
Servo yawServo;

int current_pitch;
int current_yaw;

bool setServoPosition(int pitch, int yaw) {
    /* Set the servos to the given pitch and yaw.
     * 
     * Parameters:
     *  pitch (int): PWM value for setting the angle of the pitch motor shaft.
     *  yaw (int): PWM value for setting the angle of the yaw motor shaft.
     * 
     * Returns:
     *  (bool): success of motor update
     */
    yawServo.write(yaw);
    pitchServo.write(pitch);
    return true;
}

String respondSensorMessage(String message) {
    /* Decodes sensor command messages and generates response.
     * 
     * Parameters:
     *  message (String): Data from sensor message sent over serial from python.
     * 
     * Returns:
     *  (String): message to be sent as a response
     */
    int distance = analogRead(DISTANCE_SENSOR_PIN);
    String response = String(distance, DEC);
    return response;
}

String respondServoMessage(String message) {
    /* Decodes motor command messages and generates response.
     * 
     * Parameters:
     *  message (String): Data from motor message sent over serial from python.
     * 
     * Returns:
     *  (String): message to be sent as a response
     */
    int pitch = message.substring(0, 3).toInt();
    int yaw = message.substring(4, 7).toInt();
    int waitTime = 1;
    setServoPosition(pitch, yaw);
    String response = String(waitTime, DEC);
    return response;
}

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
     * response function and returns the response.
     * 
     * Parameters:
     *  message (String): the raw message sent over serial from python.
     */
    char messageType = message.charAt(TYPE_INDEX);
    String data = message.substring(DATA_INDEX);
    String response;
    switch (messageType) {
        case 'M':
            response = respondServoMessage(data);
            sendMessage('M', response);
            break;
        case 'S':
            response = respondSensorMessage(data);
            sendMessage('S', response);
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
    current_pitch = 0;
    current_yaw = 0;
    setServoPosition(current_pitch, current_yaw);
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
