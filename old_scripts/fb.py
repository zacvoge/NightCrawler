# import libraries needed from firebaes
import pyrebase
# Configuration copied from firebase console.
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
email = 'vidsample4432@gmail.com'
pwd = '121212'

# Create test user given credentials
# Only run below line if user has not been created yet
# auth_token = auth.create_user_with_email_and_password(email, pwd)
auth_token = auth.sign_in_with_email_and_password(email, pwd)
print(auth_token['localId'])

# A user's idToken expires after 1 hour, so be sure to use the user's refreshToken to avoid stale tokens.
token_id = auth_token['idToken']

# Realtime Database Example Usage:
command = {
        'velx': 0,
        'vely': 0,
    }
