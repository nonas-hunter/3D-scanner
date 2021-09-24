void setup() {
 Serial.begin(115200);
}
void loop() {
    //for(int num = 0; num <= 1000; num += 1){
    //    Serial.println(num);
   
    if (!Serial.available()){
        char inByte = Serial.read();
        type-data = inByte.substring(stype, etype);
        data = inByte.substring(sdata, edata);
        Serial.println(inByte);
        }
    }
}