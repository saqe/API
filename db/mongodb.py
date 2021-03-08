import pymongo
from os import getenv

class MongoDB:
    def __init__(self,):
        self.client = pymongo.MongoClient(getenv('MONGODB_URI'))
        self.studentCollection  = self.client.User['Student']
        self.TeacherCollection  = self.client.User['Teacher']
        self.scheduleCollection = self.client.Classes['Schedule']

    def findStudent(self, firebase_id, parameters):
        response = self.studentCollection.find_one(
            {'firebase_user_id':firebase_id},
            parameters
        )
        return response
    
    def findTeacher(self, firebase_id, parameters):
        response = self.TeacherCollection.find_one(
            {'firebase_user_id':firebase_id},
            parameters
        )
        return response

    def findSchedules(self, firebase_id, parameters):
        response = self.scheduleCollection.find_one(
            {
                'firebase_user_id':firebase_id,
                'completed':False,
            },
            parameters
        )
        return response
    