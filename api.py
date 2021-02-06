from fastapi import FastAPI, Depends, status, HTTPException
from fastapi_cloudauth.firebase import FirebaseCurrentUser, FirebaseClaims

from auth import FirebaseAuth
from model import AuthModel
from db import DatabaseManager
from user import User

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
firebase_auth = FirebaseAuth()
get_current_user = FirebaseCurrentUser()

@app.get("/")
def index():
    return {
        'message':'Thanks for visiting the api'
    }

@app.get("/student/upcomming_classes")
def get_upcomming_classes(user: FirebaseClaims = Depends(get_current_user)):
    # user = UserModel(user[''])
    return f"Hello, {user.__dict__}"
    
@app.get("/student/profile")
def get_student_profile(user: FirebaseClaims = Depends(get_current_user)):    
    profile=User(user)
    return dict(profile.getProfile())

# Only for testing and getting the token
@app.post("/auth/login")
def login(auth: AuthModel):
    try:
        user = firebase_auth.login(auth)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication not successfull. Incorrect email or password",
        )
    return user

@app.get("/student/test/profile")
def get_student_profile():
    profile=User(FirebaseClaims(**{'user_id':'HhSLvQc0aHZYhxxoGpeJCWoB3FD2','email':''}))
    return profile.getProfile()