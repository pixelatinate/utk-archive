
int redPin = 12;
int yellowPin = 10;
int greenPin = 7;
int bluePin = 5;

int second = 1000;

void setup() {
pinMode(redPin, OUTPUT);
pinMode(yellowPin, OUTPUT);
pinMode(greenPin, OUTPUT);
pinMode(bluePin, OUTPUT);
}

void loop() {
digitalWrite(redPin, HIGH);
delay (2*second);
digitalWrite(yellowPin, HIGH);
delay (second);
digitalWrite(greenPin, HIGH);
delay (0.5*second);
digitalWrite(bluePin, HIGH);
delay (0.25*second);

digitalWrite(redPin, LOW);
digitalWrite(yellowPin, LOW);
digitalWrite(greenPin, LOW);
digitalWrite(bluePin, LOW);

delay (0.25*second);

digitalWrite(redPin, HIGH);
digitalWrite(yellowPin, HIGH);
digitalWrite(greenPin, HIGH);
digitalWrite(bluePin, HIGH);

delay (0.25*second);

digitalWrite(redPin, LOW);
digitalWrite(yellowPin, LOW);
digitalWrite(greenPin, LOW);
digitalWrite(bluePin, LOW);

delay (0.5*second);
}
