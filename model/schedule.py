from pydantic import BaseModel
from typing import List
from datetime import datetime

class ScheduleListModel(BaseModel):
    course_id       : str
    course_title    : str
    started_date    : datetime
    schedules       : List[ScheduleClassModel]
    total_class     : int
    completed_classes:int

class ScheduleClassModel(BaseModel):
    course_id   : str
    subject_id  : str
    timestamp   : datetime
    zoom_link   : str
    meeting_id  : str
    start_time  : datetime
    end_time    : datetime
    description : str
    short_description: str
    
    
