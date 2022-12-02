
import RPi.GPIO as GPIO
from time import sleep
from firebase import firebase
url = 'https://group13-night-crawler-default-rtdb.firebaseio.com'
fb = firebase.FirebaseApplication('https://group13-night-crawler-default-rtdb.firebaseio.com', None)
print(fb.get('/users/command/', None))


# Input pins for motor control
in1 = 24
in2 = 23
in3 = 17
in4 = 27

# Motor Speed Control Pins
enA = 12
enB = 13

# Setup Left Motor(s)
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
motorLeftSpeed=GPIO.PWM(enA,1000)

# Setup Right Motor(s)
GPIO.setmode(GPIO.BCM)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
motorRightSpeed=GPIO.PWM(enB,1000)

# Start motors on full power mode
motorLeftSpeed.start(100)
motorRightSpeed.start(100)


# Run Continously
while (1):

   motorDirection = fb.get('/users/command/direction', None)
   motorSpeed = fb.get('/users/command/speed', None)

   # change both motor's power to 25% power
   if(motorSpeed == "low"):
      motorLeftSpeed.ChangeDutyCycle(25)
      motorRightSpeed.ChangeDutyCycle(25)
      print("motor speed: 25%")


   # change both motor's power to 50% power
   if(motorSpeed == "medium"):
      motorLeftSpeed.ChangeDutyCycle(50)
      motorRightSpeed.ChangeDutyCycle(50)
      print("motor speed: 50%")

   # change both motor's power to 100% power
   if(motorSpeed == "high"):
      motorLeftSpeed.ChangeDutyCycle(100)
      motorRightSpeed.ChangeDutyCycle(100)
      print("motor speed: 100%")

   # turn all motors clockwise
   if(motorDirection == "forward"):
      GPIO.output(in1,GPIO.HIGH)
      GPIO.output(in2,GPIO.LOW)
      GPIO.output(in3,GPIO.HIGH)
      GPIO.output(in4,GPIO.LOW)
      print("motor direction: forward")

   # turn all motors counter-clockwise
   if(motorDirection == "backward"):
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.HIGH)
      GPIO.output(in3,GPIO.LOW)
      GPIO.output(in4,GPIO.HIGH)
      print("motor direction: backward")

   # turn motors in opposite direction to acheive turning left
   if(motorDirection == "left"):
      GPIO.output(in3,GPIO.LOW)
      GPIO.output(in4,GPIO.HIGH)
      GPIO.output(in1,GPIO.HIGH)
      GPIO.output(in2,GPIO.LOW)
      print("motor direction: left")

   # turn motors in opposite direction to acheive turning right
   if(motorDirection == "right"):
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.HIGH)
      GPIO.output(in3,GPIO.HIGH)
      GPIO.output(in4,GPIO.LOW)
      print("motor direction: right")

   # stop movement of all motors
   if(motorDirection == "stop"):
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.LOW)
      GPIO.output(in3,GPIO.LOW)
      GPIO.output(in4,GPIO.LOW)
      print("motor direction: stop")



print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")

