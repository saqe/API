from .mongodb import MongoDB
from os import getenv
from model import StudentModel

class DatabaseManager:
    def __init__(self):
        self.db = MongoDB()

    def get_student_by_firebase_id(self,firebase_id):
        response = self.db.findStudent(
            firebase_id,
            {   '_id':0,
                'username': 1,
                'full_name': 1,
                'parent_name':1,
                'email': 1,
                'phone': 1,
                'first_name':1,
                'last_name':1,
                'firebase_user_id': 1,
                'timezone': 1,
                'country': 1,
            }
        )
        student = StudentModel(**response)
        return student
    
    def get_schedule(self,firebase_id):
        response = self.db.findSchedules(
            firebase_id,
            {   
                '_id':0
            }
        )
        schedule = StudentModel(**response)
        return schedule