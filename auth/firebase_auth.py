from os import getenv
import pyrebase
from requests.exceptions import HTTPError
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

    def verify(self,token: str):
        self.auth.get_account_info(token)
    
    def login(self,auth):
        try:
            user = self.auth.sign_in_with_email_and_password(auth.email, auth.password)
            return {
                'token':user['idToken']
            }
        except HTTPError:
            rais

        
    