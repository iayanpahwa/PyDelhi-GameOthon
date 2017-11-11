#define FSR A2

int oldVal, newVal;

void setup() { 

Serial.begin(9600); //Initiate serial port

}

void loop() {
  
int oldVal = analogRead(FSR); // Read value from sensor
delay(1);
int newVal = analogRead(FSR);

if(newVal > oldVal){
  
Serial.println(newVal);
delay(1);
  
}

}
