#include <math.h>

#define MAX_LINE_LENGTH 128 // For serial read
#define MAX_CHAMBER_REGULATOR_PRESSURE 10 // Pressure in chamber regulator that corresponds to a 5V signal input
#define MAX_IPAM_REGULATOR_PRESSURE 10 // Pressure in IPAM regulators that corresponds to a 5V signal input
#define MAX_CHAMBER_ALLOWED_PRESSURE 2.5 // Maximum pressure that will be sent to the chamber
#define MAX_IPAM_ALLOWED_PRESSURE 1.5 // Maximum pressure that will be sent to the IPAMs
#define INPUT_PRESSURE 30
#define ZERO_CONTRACTION_PRESSURE 0 // Pressure that leads to zero contraction in actuators
#define PRESSURE_SLOPE 60 // Negative of slope of pressure v. contraction curve
#define MAX_ALLOWED_PRESSURE 1.5 // Maximum pressure that will be sent to the IPAMs
#define CONTRACTION_TO_POSITION 180 // Number of centimeters that increasing contraction from 0 to 1 moves robot tip
#define PSI1 PI/6 // Angle counterclockwise from horizontal to actuator 1 when looking from base to tip of robot 
#define PSI2 5*PI/6 // Angle counterclockwise from horizontal to actuator 2 when looking from base to tip of robot
#define PSI3 3*PI/2 // Angle counterclockwise from horizontal to actuator 3 when looking from base to tip of robot
float CONTRACTION_TOLERANCE = 0.01; // Amount that we will allow minimum contraction to be greater than 0
float A = CONTRACTION_TO_POSITION*cos(PSI1); // Constants for linear algebra equation relating position to contraction
float B = CONTRACTION_TO_POSITION*cos(PSI2);
float C = CONTRACTION_TO_POSITION*cos(PSI3);
float E = CONTRACTION_TO_POSITION*sin(PSI1);
float F_CONST = CONTRACTION_TO_POSITION*sin(PSI2);
float G = CONTRACTION_TO_POSITION*sin(PSI3);

float c1 = 0; // Desired contraction in actuator 1 (0-1)
float c2 = 0; // Desired contraction in actuator 2 (0-1)
float c3 = 0; // Desired contraction in actuator 3 (0-1)

float changePressureAmount = 0.1; // Amount to change pressure for each key press; units of PSI
int changeSpeedAmount = 100; // Amount to change desired speed for each key press; units of ticks/sec
bool ESTOP = false;
// Pin Declares
const int encoderPinA = 2;
const int encoderPinB = 6;
volatile long encoderTicks = 0;
uint8_t prevAB = 0;

int motorPWMPin = 5;
int motorDirPin1 = 12;
int pressureChamberPin = 10; //11
int pressureChamberReadPin = A5; // A5
int ipam1Pin = 3; // 9
int ipam1ReadPin = A2; // A2
int ipam2Pin = 9; //10
int ipam2ReadPin = A3; // A3
int ipam3Pin = 11; // 3
int ipam3ReadPin = A4; // A4

// Variables/constants for speed control
int desiredSpeed = 0; // in units of ticks per second
double desiredPressure = 0;
double ticks0 = 0; // encoder cumulative ticks value now
double ticks1 = 0; // encoder cumulative ticks value from 1 loop ago
long time0 = 0; // time since program start now
long time1 = -1; // time since program start from 1 loop ago
double actualSpeed = 0; // in units of ticks per second
double errorSpeed = 0; // desired minus actual speed
double dutyCycle = 0; // requested duty cycle (ranges from -255 to 255)
// For loop rate of approximately 10 Hz, 0.02 seems good for kp and 0.04 seems good for ki
double kp = 0.0001; // proportional constant for PI controller (duty cycle/(ticks/sec))
double ki = 0.0001; // 0.0001 seems okay; integral constant for PI controller (duty cycle/(ticks/sec))
double fTerm = 0; // feedforward term of controller
double pTerm = 0; // proportional term of PI controller 
double iTerm = 0; // integral term of PI controller
int maxDuty = 250; // maximum allowed duty cycle magnitude

// Variables/constants for pressure control
float pc = 0; // Desired pressure in chamber
float p1 = 0; // Desired pressure in actuator 1
float p2 = 0; // Desired pressure in actuator 2
float p3 = 0; // Desired pressure in actuator 3
// Variables/constants for actual pressure in chambers/regulators
float pc_actual = 0;
float p1_actual = 0;
float p2_actual = 0;
float p3_actual = 0;
int analogWriteCounts = 255; // Maximum number that can be sent to analogWrite()
char *strings[9]; // an array of pointers to the pieces of the above array after strtok()
char *ptr = NULL;

// Serial buffer
char serialBuffer[MAX_LINE_LENGTH];
uint8_t serialIndex = 0;
unsigned long lastSerialTime = 0;
unsigned long serialTimeoutMs = 10;
bool commandActive = false;

void setup() {
  Serial.begin(115200);
    // Set up pins for pressure control
  pinMode(pressureChamberPin, OUTPUT);
  pinMode(ipam1Pin, OUTPUT);
  pinMode(ipam2Pin, OUTPUT);
  pinMode(ipam3Pin, OUTPUT);

  // setPwmFrequency(pressureChamberPin,8);
  // setPwmFrequency(ipam1Pin,8);
  // setPwmFrequency(ipam2Pin,8);
  // setPwmFrequency(ipam3Pin,8);

  analogWrite(pressureChamberPin, (pc * analogWriteCounts/MAX_CHAMBER_REGULATOR_PRESSURE));
  analogWrite(ipam1Pin, (p1 * analogWriteCounts/MAX_IPAM_REGULATOR_PRESSURE));
  analogWrite(ipam2Pin, (p2 * analogWriteCounts/MAX_IPAM_REGULATOR_PRESSURE));
  analogWrite(ipam3Pin, (p3 * analogWriteCounts/MAX_IPAM_REGULATOR_PRESSURE));
  
  // Set up pins for motor and encoder control
  pinMode(motorPWMPin, OUTPUT);
  pinMode(motorDirPin1, OUTPUT);
  // Initialize the encoder pins
  pinMode(encoderPinA, INPUT);
  pinMode(encoderPinB, INPUT);
  // Initialize encoder state
  prevAB = (digitalRead(encoderPinA) << 1) | digitalRead(encoderPinB);
  setDuty();
}

void updateEncoder() {
  uint8_t currentAB = (digitalRead(encoderPinA) << 1) | digitalRead(encoderPinB);

  const int8_t encoder_table[4][4] = {
    {  0,  1, -1,  0},
    { -1,  0,  0,  1},
    {  1,  0,  0, -1},
    {  0, -1,  1,  0}
  };

  encoderTicks += encoder_table[prevAB][currentAB];
  prevAB = currentAB;
}

// --------------------------
// Set PWM Freq 
// --------------------------
// void setPwmFrequency(int pin, int divisor) {
//   byte mode;
//   if(pin == 5 || pin == 6 || pin == 9 || pin == 10) {
//     switch(divisor) {
//       case 1: mode = 0x01; break;
//       case 8: mode = 0x02; break;
//       case 64: mode = 0x03; break;
//       case 256: mode = 0x04; break;
//       case 1024: mode = 0x05; break;
//       default: return;
//     }
//     if(pin == 5 || pin == 6) {
//       TCCR0B = TCCR0B & 0b11111000 | mode;
//     } else {
//       TCCR1B = TCCR1B & 0b11111000 | mode;
//     }
//   } else if(pin == 3 || pin == 11) {
//     switch(divisor) {
//       case 1: mode = 0x01; break;
//       case 8: mode = 0x02; break;
//       case 32: mode = 0x03; break;
//       case 64: mode = 0x04; break;
//       case 128: mode = 0x05; break;
//       case 256: mode = 0x06; break;
//       case 1024: mode = 0x07; break;
//       default: return;
//     }
//     TCCR2B = TCCR2B & 0b11111000 | mode;
//   }
// }

void loop() {
  // Updates xTip, yTip, zTip, analog_value, pressure_pot_value, and reverse_value
  handleSerial();
  // checkTimeout();
  // Convert current and desired robot speed to duty cycle, and send to motor
  calcAndSetDuty();
  // Send desired pressures to pressure regulators
  setPressures();
  // Read pressures from analog pins
  readPressures();
  // Send the state back through the serial port
  sendState();
  delay(10); // ~100Hz
}

void handleSerial() {
  while (Serial.available() > 0) {
    char inChar = Serial.read();
    lastSerialTime = millis();

    if (inChar == '\n') {
      serialBuffer[serialIndex] = '\0';

      if (serialIndex > 0) {
        // Serial.print("Received line: ");
        // Serial.println(serialBuffer);  // Print the complete received line

        parseCommand(String(serialBuffer));
        commandActive = true;
      }

      serialIndex = 0;
    } 
    else if (inChar != '\r') {
      if (serialIndex < MAX_LINE_LENGTH - 1) {
        serialBuffer[serialIndex++] = inChar;
      } else {
        serialIndex = 0;
      }
    }
  }
}


void checkTimeout() {
  if (millis() - lastSerialTime > serialTimeoutMs && commandActive) {
    desiredSpeed = 0;
    pc = p1 = p2 = p3 = 0;
    commandActive = false;
  }
}

void parseCommand(String command) {
  // Serial.print("parseCommand called with: ");
  // Serial.println(command);

  if (!command.startsWith("SET")) {
    // Serial.println("Command does not start with 'SET', ignoring.");
    return;
  }

  command.remove(0, 4);  // Remove "SET,"

  float values[10] = {0};
  int idx = 0;
  while (command.length() > 0 && idx < 10) {
    int commaIndex = command.indexOf(',');
    String value = (commaIndex != -1) ? command.substring(0, commaIndex) : command;
    values[idx++] = value.toFloat();

    // Serial.print("Parsed value ");
    // Serial.print(idx - 1);
    // Serial.print(": ");
    // Serial.println(values[idx - 1], 6);

    if (commaIndex == -1) break;
    command.remove(0, commaIndex + 1);
  }

  if (idx < 9) {
    // Serial.print("Warning: Expected 9 or more values, got ");
    // Serial.println(idx);
  }

  // Assign parsed values to variables
  int rb         = (int)values[0];
  int dpad_down  = (int)values[1];
  int dpad_up    = (int)values[2];
  int triangle   = (int)values[3];
  int x          = (int)values[4];
  int square     = (int)values[5];
  int circle     = (int)values[6];
  float y_joy    = values[7] * 5.0;         // Amplify for actuator control
  float x_joy    = values[8] * 5.0 * -1.0;  // Inverted for consistency

  // Serial.print("rb: "); Serial.println(rb);
  // Serial.print("dpad_down: "); Serial.println(dpad_down);
  // Serial.print("dpad_up: "); Serial.println(dpad_up);
  // Serial.print("triangle: "); Serial.println(triangle);
  // Serial.print("x: "); Serial.println(x);
  // Serial.print("square: "); Serial.println(square);
  // Serial.print("circle: "); Serial.println(circle);
  // Serial.print("y_joy: "); Serial.println(y_joy, 6);
  // Serial.print("x_joy: "); Serial.println(x_joy, 6);

  // Change chamber pressure
  if (triangle == 1) {
    pc += 0.1;
    Serial.println("Triangle pressed: Increasing chamber pressure");
  }
  if (x == 1) {
    pc -= 0.1;
    Serial.println("X pressed: Decreasing chamber pressure");
  }

  // Change grow speed
  if (dpad_up == 1) {
    desiredSpeed += 100;
    // Serial.println("Dpad Up pressed: Increasing desired speed");
  }
  if (dpad_down == 1) {
    desiredSpeed -= 100;
    // Serial.println("Dpad Down pressed: Decreasing desired speed");
  }
  if (square == 1) {
    desiredSpeed = 0;
    // Serial.println("Square pressed: Stopping robot");
  }

  // Kill actuator pressure
  if (rb == 1) {
    p1 = p2 = p3 = 0.0;
    // Serial.println("RB pressed: Killing actuator pressure");
    return;
  }

  // Joystick curvature control
  if ((x_joy != 0.0) || (y_joy != 0.0)) {
    c3 = 0;
    calculateCurvatures(x_joy, y_joy);
    // Serial.print("Initial curvatures: c1=");
    // Serial.print(c1, 6);
    // Serial.print(", c2=");
    // Serial.print(c2, 6);
    // Serial.print(", c3=");
    // Serial.println(c3, 6);

    while ((minimum(c1, c2, c3) < 0) || (minimum(c1, c2, c3) > CONTRACTION_TOLERANCE)) {
      float minVal = minimum(c1, c2, c3);
      c3 += (minVal < 0) ? 0.2 * CONTRACTION_TOLERANCE : -0.2 * CONTRACTION_TOLERANCE;
      calculateCurvatures(x_joy, y_joy);
      // Serial.print("Adjusted c3: ");
      // Serial.print(c3, 6);
      // Serial.print(", c1=");
      // Serial.print(c1, 6);
      // Serial.print(", c2=");
      // Serial.print(c2, 6);
      // Serial.print(", c3=");
      // Serial.println(c3, 6);
    }

    p1 = PRESSURE_SLOPE * c1 + ZERO_CONTRACTION_PRESSURE;
    p2 = PRESSURE_SLOPE * c2 + ZERO_CONTRACTION_PRESSURE;
    p3 = PRESSURE_SLOPE * c3 + ZERO_CONTRACTION_PRESSURE;
    p1 = min(p1, MAX_ALLOWED_PRESSURE);
    p2 = min(p2, MAX_ALLOWED_PRESSURE);
    p3 = min(p3, MAX_ALLOWED_PRESSURE);

    // Serial.print("Final pressures: p1=");
    // Serial.print(p1, 6);
    // Serial.print(", p2=");
    // Serial.print(p2, 6);
    // Serial.print(", p3=");
    // Serial.println(p3, 6);
  }
  sendState();
}


void calculateCurvatures(float x, float y) {
  // Helper function for sendPressures() that calculates c1 and c2 based on constants, c3, xRobot, and yRobot
  c1 = -((C - (B * G / F_CONST)) / (A - (B * E / F_CONST)) * c3) + ((x - (B * y / F_CONST)) / (A - (B * E / F_CONST)));
  c2 = -((C - (A * G / E)) / (B - (A * F_CONST / E)) * c3) + ((x - (A * y / E)) / (B - (A * F_CONST / E)));
}

void readPressures() {
    // Read values from output line and report values rescaled relative to the input pressures
  pc_actual = map(analogRead(pressureChamberReadPin) * 2, 0, 5, 0, INPUT_PRESSURE);
  p1_actual = map(analogRead(ipam1ReadPin) * 2, 0, 5, 0, INPUT_PRESSURE);
  p2_actual = map(analogRead(ipam2ReadPin) * 2, 0, 5, 0, INPUT_PRESSURE);
  p3_actual = map(analogRead(ipam3ReadPin) * 2, 0, 5, 0, INPUT_PRESSURE);
}

void sendState() {
  char buffer[128];

  // Temp string buffers for float values
  char pc_actual_str[10], pc_str[10];
  char p1_actual_str[10], p1_str[10];
  char p2_actual_str[10], p2_str[10];
  char p3_actual_str[10], p3_str[10];
  char dutyCycle_str[10];

  // Convert float to string
  dtostrf(pc_actual, 6, 3, pc_actual_str);
  dtostrf(pc,        6, 3, pc_str);
  dtostrf(p1_actual, 6, 3, p1_actual_str);
  dtostrf(p1,        6, 3, p1_str);
  dtostrf(p2_actual, 6, 3, p2_actual_str);
  dtostrf(p2,        6, 3, p2_str);
  dtostrf(p3_actual, 6, 3, p3_actual_str);
  dtostrf(p3,        6, 3, p3_str);
  dtostrf(dutyCycle, 6, 3, dutyCycle_str);

  // Now format into buffer
  snprintf(buffer, sizeof(buffer),
           "STATE,%s,%s,%s,%s,%s,%s,%s,%s,%d,%s",
           pc_actual_str, pc_str,
           p1_actual_str, p1_str,
           p2_actual_str, p2_str,
           p3_actual_str, p3_str,
           desiredSpeed, dutyCycle_str);

  Serial.println(buffer);
}

void setPressures() {
   // Cap desired pressures between the maximum and minimum allowed
  pc = constrain(pc, 0, MAX_CHAMBER_ALLOWED_PRESSURE);
  p1 = constrain(p1, 0, MAX_IPAM_ALLOWED_PRESSURE);
  p2 = constrain(p2, 0, MAX_IPAM_ALLOWED_PRESSURE);
  p3 = constrain(p3, 0, MAX_IPAM_ALLOWED_PRESSURE);
  analogWrite(pressureChamberPin, (pc * analogWriteCounts/MAX_CHAMBER_REGULATOR_PRESSURE));
  analogWrite(ipam1Pin, (p1 * analogWriteCounts/MAX_IPAM_REGULATOR_PRESSURE));
  analogWrite(ipam2Pin, (p2 * analogWriteCounts/MAX_IPAM_REGULATOR_PRESSURE));
  analogWrite(ipam3Pin, (p3 * analogWriteCounts/MAX_IPAM_REGULATOR_PRESSURE));
}

void calcAndSetDuty() {
  // Read encoder ticks
  updateEncoder();
  ticks0 = encoderTicks;
  // Read current time
  time0 = micros();
  // Update speed
  actualSpeed = 1000000*(ticks0-ticks1)/(time0-time1);
  errorSpeed = desiredSpeed - actualSpeed;
  if (desiredSpeed > 0) {
    fTerm = 0.4*desiredSpeed + 10;
  } else if (desiredSpeed < 0) {
    fTerm = 0.4*desiredSpeed - 30;
  } else {
    fTerm = 15; // bias to retract
  }
  pTerm = kp*errorSpeed;
  iTerm += ki*errorSpeed;
  dutyCycle = fTerm + pTerm + iTerm;
  if (dutyCycle < 0) {
    if (dutyCycle < -125) {
      dutyCycle = -125;
      }
    iTerm -= ki*errorSpeed;
  } else if (dutyCycle > maxDuty) {
    dutyCycle = maxDuty;
    iTerm -= ki*errorSpeed;
  }
  
  if (desiredSpeed == 0) {
    dutyCycle = 0;
    }
  setDuty();

  time1 = time0;
  ticks1 = ticks0;
}

void setDuty() {
  if (dutyCycle >= 0) {
    // Cap at 255
    dutyCycle = min(dutyCycle, 255);
    digitalWrite(motorDirPin1, HIGH); //High
    analogWrite(motorPWMPin, dutyCycle);
  } else {
    // Cap at -255
    dutyCycle = max(dutyCycle, -255);
    digitalWrite(motorDirPin1, LOW);
    analogWrite(motorPWMPin, -dutyCycle);
  }
}

float minimum(float a, float b, float c) {
  // Takes the minimum of three floating point numbers
  return min(a, min(b, c));
}