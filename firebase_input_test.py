
from time import sleep
from firebase import firebase
url = 'https://group13-night-crawler-default-rtdb.firebaseio.com'
fb = firebase.FirebaseApplication('https://group13-night-crawler-default-rtdb.firebaseio.com', None)


motorSpeedPrevious = fb.get('/users/command/motor_speed/speed', None)
# Run Continously
while (True):

   motorDirection = fb.get('/users/command/motor/direction', None)
   motorSpeed = fb.get('/users/command/motor_speed/speed', None)
   servoDirection = fb.get('/users/command/servo/direction', None)

   # change both motor's power to 25% power
   if(motorSpeed == "low" and motorSpeedPrevious != motorSpeed):
      print("motor speed: 25%")

   # change both motor's power to 50% power
   if(motorSpeed == "medium" and motorSpeedPrevious != motorSpeed):
      print("motor speed: 50%")

   # change both motor's power to 100% power
   if(motorSpeed == "high" and motorSpeedPrevious != motorSpeed):
      print("motor speed: 100%")

   # turn all motors clockwise
   if(motorDirection == "forward" ):
      print("motor direction: forward")

   # turn all motors counter-clockwise
   if(motorDirection == "backward"):
      print("motor direction: backward")

   # turn motors in opposite direction to acheive turning left
   if(motorDirection == "left"):
      print("motor direction: left")

   # turn motors in opposite direction to acheive turning right
   if(motorDirection == "right"):
      print("motor direction: right")

   # disable for now for readability
   # if(motorDirection == "stop"):
   #    print("stop")

   if(servoDirection == "left"):
      print("pan left")

   if(servoDirection == "right"):
      print("pan right")

   if(servoDirection == "up"):
      print("tilt up")

   if(servoDirection == "down"):
      print("tilt down")

   motorSpeedPrevious = motorSpeed


   sleep(1)



