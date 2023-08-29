from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()



# MONGODB CONNECTION SECTION USING PYMONGO
mongo_uri                   = os.getenv("MONGO_URI")
client                      = MongoClient(mongo_uri)
register_new_student        = client.zenith_DB.students
register_new_tutor          = client.zenith_DB.teachers
