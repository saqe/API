from pydantic import BaseModel
from pytz import all_timezones

class StudentModel( BaseModel ):
    username    : str
    full_name   : str
    first_name  : str
    last_name   : str
    parent_name : str
    email       : str
    phone       : str
    timezone    : 'Australia/Sydney'
    country     : str