from db import DatabaseManager
from model import StudentModel

class User:
    def __init__(self, user):
        # Model received in Construcutor
        self.user = user
        # Connection with database
        self.db = DatabaseManager()

    def getProfile(self) :
        student=self.db.get_student_by_firebase_id(self.user.user_id)
        return student
    
    def getStudentDashboard(self):
        pass