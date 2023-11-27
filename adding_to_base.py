from models import *
from peewee import *
from api_sibur import person, comments

 
with connection:
    Persons.insert_many(person).execute()
    Comments.insert_many(comments).execute()

print("Done")