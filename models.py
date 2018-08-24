from app import db 
import datetime 
from config import Configuration 
import re

# class Test(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.String(80))

#     def __init__(self,*args,**kwargs):
#         super(Test,self).__init__(*args,**kwargs)

# def slugify(name):
#     return re.sub('[^\w]+','-',name).lower()


class Person(db.Model):


	
    id = db.Column(db.Integer,primary_key=True)
    image_id = db.Column(db.String(20),nullable=False)
    name = db.Column(db.String(60),unique=True,nullable=False)
    slug = db.Column(db.String(60),unique=True)
    person_type = db.Column(db.String(50),nullable=False)
    biography = db.Column(db.Text,nullable=False)
    created_timestamp = db.Column(db.DateTime,default=datetime.datetime.now())
    rating = db.Column(db.Float,default=0.0)


    def __init__(self,*args,**kwargs):
        super(Person,self).__init__(*args,**kwargs)
        

    def read_more(self):
        return self.biography[:42] + " ..."
        


