
  GNU nano 5.4                                      app_controllers.py                                               
import RPi.GPIO as GPIO
from time import sleep
import wiringpi
import pyrebase
from firebase import firebase
url = 'https://group13-night-crawler-default-rtdb.firebaseio.com'
fb = firebase.FirebaseApplication('https://group13-night-crawler-default-rtdb.firebaseio.com', None)
print(fb.get('/users/command/', None))


in1 = 24
in2 = 23
in3 = 17
in4 = 27
enA = 12
enB = 13
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(enA,1000)

GPIO.setmode(GPIO.BCM)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
pb=GPIO.PWM(enB,1000)


p.start(100)
pb.start(100)


# Firebase test
auth_token = auth.sign_in_with_email_and_password(uname, pwd)
message.set('Success')
auth_message.set('auth_token: ' + auth_token['localId'])
login_message.set('Logout')
path_local = "test_video.mp4"

# Implementation of FIREBASE STORAGE
path_on_cloud = 'users/' + auth_token['localId'] + '/videos/' + path_local
print(path_on_cloud)


#Upload Sample Video to firebase storage
storage = firebase.storage()

while (1):

   direction = fb.get('/users/command/direction', None)

   # clockwise
   if(direction == "forward"):
      GPIO.output(in1,GPIO.HIGH)
      GPIO.output(in2,GPIO.LOW)
      GPIO.output(in3,GPIO.HIGH)
      GPIO.output(in4,GPIO.LOW)
      print("forward")

   if(direction == "backward"):
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.HIGH)
      GPIO.output(in3,GPIO.LOW)
      GPIO.output(in4,GPIO.HIGH)
      print("backward")

   if(direction == "left"):
      GPIO.output(in3,GPIO.LOW)
      GPIO.output(in4,GPIO.HIGH)
      GPIO.output(in1,GPIO.HIGH)
      GPIO.output(in2,GPIO.LOW)

   if(direction == "right"):
      GPIO.output(in3,GPIO.HIGH)
      GPIO.output(in4,GPIO.LOW)
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.HIGH)

   if(direction == "stop"):
      print("stop")
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.LOW)
      GPIO.output(in3,GPIO.LOW)
      GPIO.output(in4,GPIO.LOW)



print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")

