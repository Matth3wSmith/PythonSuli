
int motor1=23;
int motor2=22;
int button1=34;
int button2=35;


struct {
   unsigned long t100ms;
   unsigned long t1000ms;
}prevMillis;
unsigned long currentMillis;

void setup(){
  	
	lcd.begin(16,2);
  pinMode(22,OUTPUT);
  pinMode(23,OUTPUT);
  pinMode(35,INPUT);
  pinMode(34,INPUT);

};

void loop(){

  if (digitalRead(button1)==HIGH){
    digitalWrite(motor1,HIGH);
  }
  else{
    digitalWrite(motor1,LOW);
  };
  if (digitalRead(button2)==HIGH){
    digitalWrite(motor2,HIGH);
  }
  else{
    digitalWrite(motor2,LOW);
  };
  

}