
const int buttonPin1 = 10; 
const int buttonPin2 = 11;
const int buttonPin3 = 12;  
const int ledPin =  LED_BUILTIN;


void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin1, INPUT_PULLUP);
pinMode(buttonPin2, INPUT_PULLUP);  
pinMode(buttonPin3, INPUT_PULLUP); 
}

void loop() {
 

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (digitalRead(buttonPin1) == HIGH) {
  Serial.println('1');
  digitalWrite(ledPin, HIGH);
  } 
  
  else if (digitalRead(buttonPin2) == HIGH){
      Serial.println('2');
      digitalWrite(ledPin, HIGH);
  }
 else if (digitalRead(buttonPin3) == HIGH){
      Serial.println('3');
      digitalWrite(ledPin, HIGH);
  }  
  else {
    // turn LED off:
    digitalWrite(ledPin, LOW);
  }
delay(300);
}
