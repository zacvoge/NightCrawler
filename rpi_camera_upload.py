import pyrebase
config = {
  'apiKey': "AIzaSyD-8O8ys8bwF4N4-bGavw5KwziaHwELVNU",
  'authDomain': "group13-night-crawler.firebaseapp.com",
  'databaseURL': "https://group13-night-crawler-default-rtdb.firebaseio.com",
  'projectId': "group13-night-crawler",
  'storageBucket': "group13-night-crawler.appspot.com",
  'messagingSenderId': "52466109472",
  'appId': "1:52466109472:web:3f22774086f5053cd74045",
  'measurementId': "G-QN54Z2X23D"
}



# Initialize firebase with config copied from firebase console
firebase = pyrebase.initialize_app(config);


# Create reference to firauth service
auth = firebase.auth();

# Make reference to firebase realtime database
# - this will be responsible for moving the servo from application
db = firebase.database();

# Test username and password
# email = 'vidsample4432@gmail.com'
# pwd = '121212'

auth_token = auth.sign_in_with_email_and_password("vidsample4432@gmail.com", "121212")
path_local = "videos/sample_video_1.mp4"

# Implementation of FIREBASE STORAGE
path_on_cloud = 'users/' + auth_token['localId'] + '/' + path_local
print(path_on_cloud)


#Upload Sample Video to firebase storage
storage = firebase.storage()
storage.child(path_on_cloud).put(path_local)

print("Attempted Uploaded of " + path_local)


