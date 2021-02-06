from fastapi import FastAPI, Depends
from fastapi_cloudauth.firebase import FirebaseCurrentUser, FirebaseClaims

app = FastAPI()

get_current_user = FirebaseCurrentUser()

@app.get("/student/getclasses")
def secure_user(current_user: FirebaseClaims = Depends(get_current_user)):
    return f"Hello, {current_user.__dict__}"
    