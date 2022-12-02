
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
print ("Waiting for 2 seconds")
time.sleep(2)

#Let's move the servo!
print ("Rotating 180 degrees in 10 steps")

# Define variable duty
duty = 2


while duty <= 2:
    servo2.ChangeDutyCycle(duty)
    time.sleep(1)
    duty = duty + 1

# Loop for duty values from 2 to 12 (0 to 180 degrees)
while duty <= 7:
    servo1.ChangeDutyCycle(duty)
    time.sleep(1)
    duty = duty + 1





# Wait a couple of seconds
time.sleep(2)

# Turn back to 90 degrees
print ("Turning back to 90 degrees for 2 seconds")
servo1.ChangeDutyCycle(7)
servo2.ChangeDutyCycle(7)
time.sleep(2)

#turn back to 0 degrees
print ("Turning back to 0 degrees")
servo1.ChangeDutyCycle(2)
servo2.ChangeDutyCycle(2)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)
servo2.ChangeDutyCycle(0)

#Clean things up at the end
servo1.stop()
servo2.stop()
GPIO.cleanup()
print ("Goodbye")

