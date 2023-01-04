int n_led_builtin = 13;
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(n_led_builtin, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(n_led_builtin, HIGH);   // turn the LED on 
  delay(111);                       // wait for half a second
  digitalWrite(n_led_builtin, LOW);    // turn the LED off 
  delay(111);                       // wait for half a second
}