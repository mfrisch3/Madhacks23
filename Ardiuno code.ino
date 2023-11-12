void setup() {
    Serial.begin(9600); // Start the serial communication at 9600 baud rate
}

void loop() {
    if (Serial.available() > 0) {
        int number = Serial.parseInt(); // Read the incoming number
        if (number > 0) {
            // Code to display a smiley
        } else {
            // Code to display something else
        }
    }
}