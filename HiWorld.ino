const int blanco=13;


void setup() 
{
  Serial.begin(9600);
  pinMode(blanco, OUTPUT);
  // put your setup code here, to run once:

}

void loop() {
  if (Serial.available()>0)
  {
    char option = Serial.read();
    if (option>='1' && option<='9'){
      option-='0';
      for (int i=0;i<option;i++){
        digitalWrite(blanco, HIGH);
        delay(100);
        digitalWrite(blanco, LOW);
        delay(200);
      }
    }
  }
  Serial.println("Hola Mundo");
  delay(1000);
  // put your main code here, to run repeatedly:

}
