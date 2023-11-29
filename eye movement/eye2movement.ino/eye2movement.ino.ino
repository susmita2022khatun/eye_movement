const int IRpin = A0;
const int led = 13;

float reading;
float p_reading;

bool isDone = false;
int count = 0;
bool state;

long time1;
long time2;
long time3;


void setup() {
  pinMode(IRpin, INPUT);
  pinMode(led, OUTPUT);
  pinMode(A1, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  reading = analogRead(IRpin);
  Serial.println(reading);
  digitalWrite(A1, HIGH);

  if(reading > 200){
    reading = 700;
  }


  if(p_reading > reading + 300 || p_reading < reading - 300){
    Serial.print("Reading:");
    Serial.println(reading);
    p_reading = reading;

    if(p_reading < 200){
      state = true;
      digitalWrite(led, HIGH);
      
    }else{
      state = false;
      digitalWrite(led, LOW );
    }
    if (state && isDone == false && millis() > 3000){
      time1 = millis();
      time3 = time1;
      count = 1;
      isDone = true;
    }else if(state && isDone == true){
      time2 = millis();
      if((time2 - time1) < 1500 && (time2 - time1) > 200){
        count++;
        time1 = time2;
      }
    
    }
  }

  if((millis() - time3) > 2500){
    if(count != 0){
      Serial.print("Count: ");
      Serial.println(count); 
    
    count = 0;
    isDone = false;
    time3 = millis();
    time1 = 0;
    time2 = 0;
    }
    
  }



delay(100);
    
}
