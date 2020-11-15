const int blanco=13;


void setup() 
{
  Serial.begin(9600);
  pinMode(blanco, OUTPUT);
  // put your setup code here, to run once:

}

void loop() {
  
        digitalWrite(blanco, HIGH);
        delay(1000);
        Serial.println("Encendido");
        digitalWrite(blanco, LOW);
        Serial.println("Apagado");
        delay(500);
      
    
  
  Serial.println("Hola Mundo");
  delay(1000);
  // put your main code here, to run repeatedly:

}
