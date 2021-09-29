uint16_t LOOP_INTERVAL = 20;
uint32_t loop_time;
int distancesensor = 0;

bool it_is_time(uint32_t t, uint32_t t0, uint16_t dt) {
  return ((t >= t0) && (t - t0 >= dt)) ||         // The first disjunct handles the normal case
            ((t < t0) && (t + (~t0) + 1 >= dt));  //   while the second handles the overflow case
}

void setup() {
  Serial.begin(115200);
  
  loop_time = millis();
}

void loop() {
  uint32_t t;
  uint16_t x, y, z, res;
  
  t = millis();
  if (it_is_time(t, loop_time, LOOP_INTERVAL)) {
    x = analogRead(distancesensor);
    y = analogRead(distancesensor);
    z = analogRead(distancesensor);

    //res = x;
    //res = (x + y + z) / 3;
    res = min(min(x, y), z);
    Serial.println(res);

    loop_time = t;
  }
}