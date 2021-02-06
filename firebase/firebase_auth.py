from os import getenv
from dotenv import load_dotenv
load_dotenv()
import pyrebase

class FirebaseAuth:
    def __init__(self):
        firebaseConfig = {
            'apiKey':           getenv('firebase_apiKey'),
            'authDomain':       getenv('firebase_authDomain'),
            'databaseURL':      getenv('firebase_databaseURL'),
            'projectId':        getenv('firebase_projectId'),
            'storageBucket':    getenv('firebase_storageBucket'),
            'messagingSenderId':getenv('firebase_messagingSenderId'),
            'appId':            getenv('firebase_appId'),
        }
        firebase = pyrebase.initialize_app(firebaseConfig)
        self.auth = firebase.auth()

    def verify(self,token):
        self.auth.get_account_info(token)
    
    def get_user(self,token):
        self.auth.get_account_info(token)