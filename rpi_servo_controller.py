
import RPi.GPIO as GPIO
from time import sleep
from firebase import firebase
url = 'https://group13-night-crawler-default-rtdb.firebaseio.com'
fb = firebase.FirebaseApplication('https://group13-night-crawler-default-rtdb.firebaseio.com', None)
print(fb.get('/users/command/', None))

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 tilt output pin
GPIO.setup(40,GPIO.OUT)
pan = GPIO.PWM(40,50) # Note 11 is pin, 50 = 50Hz pulse

#Setup pin 36 as pan pin
GPIO.setup(36,GPIO.OUT)
tilt = GPIO.PWM(36,50)

#start PWM running, but with value of 0 (pulse off)
pan.start(0)
tilt.start(0)

#Let's move the servo!
print ("Rotating 180 degrees in 10 steps")

# Method 2
# panDutyCycle = 7.5
# tiltDutyCycle = 7.5


while(True):

   # Get movement command of the servo
   servoDirection = fb.get('/users/command/servo/direction', None)

   # left -90 deg position
   if(servoDirection == "left"):
      # method 2
      # panDutyCycle -= 1
      # pan.ChangeDutyCycle(panDutyCycle)
      # sleep(1)
      print("pan left")
      pan.ChangeDutyCycle(5)
      sleep(1)

   # right +90 deg position
   if(servoDirection == "right"):
      # method 2
      # panDutyCycle += 1
      # pan.ChangeDutyCycle(panDutyCycle)
      # sleep(1)
      print("pan right")
      pan.ChangeDutyCycle(10)
      sleep(1)

   if(servoDirection == "up"):
      # method 2
      # tiltDutyCycle -= 1
      # tilt.ChangeDutyCycle(tiltDutyCycle)
      # sleep(1)
      print("tilt up")
      tilt.ChangeDutyCycle(5)
      sleep(1)

   if(servoDirection == "down"):
      # method 2
      # tiltDutyCycle += 1
      # tilt.ChangeDutyCycle(tiltDutyCycle)
      # sleep(1)
      print("tilt down")
      tilt.ChangeDutyCycle(10)
      sleep(1)
