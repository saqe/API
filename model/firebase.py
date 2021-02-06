
from pydantic import BaseModel

class AuthModel(BaseModel):
    email: str
    password: str

class FirebaseAuthUser(BaseModel):
    user_id: str
    email: str