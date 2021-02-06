import pymongo
from os import getenv

class MongoDB:
    def __init__(self,):
        self.client = pymongo.MongoClient(getenv('MONGODB_URI'))
        self.studentCollection = self.client.User['Student']
    
    def findStudent(self,firebase_id,parameters):
        response = self.studentCollection.find_one(
            {'firebase_user_id':firebase_id},
            parameters
        )
        return response
    
    def 
    
