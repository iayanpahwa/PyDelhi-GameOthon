#define FSR A2
#define startButton 3
#define statusStart 13
volatile byte state = LOW;

int oldVal, newVal;

void setup() { 

  pinMode(statusStart, OUTPUT);
  pinMode(startButton, INPUT_PULLUP);
  Serial.begin(9600); //Initiate serial port
  attachInterrupt(digitalPinToInterrupt(startButton), start, LOW);
}

void start(){

  state = HIGH;
  
}

void loop() {

  digitalWrite(statusStart, state);
  int oldVal = analogRead(FSR); // Read value from sensor
  delay(1);
  int newVal = analogRead(FSR);

if(newVal > oldVal){
  int newVal = analogRead(FSR);
  Serial.println(newVal);  
  delay(100);
}

}
