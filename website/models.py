from flask_login import UserMixin
from sqlalchemy.sql import func 
from .helper_db import db 
import random


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    # func: get the current date and time and store 
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_title = db.Column(db.String(250), nullable=False)
    credit = db.Column(db.Integer, nullable=False)
    course_number = db.Column(db.Integer, unique=True, nullable=False) 
    course_date  = db.Column(db.DateTime(timezone=True), default=func.now())    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def generate_course_number():
        # generate 4-digits long integer
        return random.randint(1000, 9999)
    def genrate_course_credit():
        # generate between 1-4digits long integer 
        return random.randint(1, 4)
   
    
    
class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    csc_department = db.Column(db.String(250), nullable=False)
    bis_departmrnt = db.Column(db.String(250), nullable=False)
    sci_departmrnt = db.Column(db.String(250), nullable=False)
    phi_departmrnt = db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Major(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    csc_major = db.Column(db.String(250))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile = db.Column(db.LargeBinary)
    url = db.Column(db.String(250))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class GeneralInformation(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    student_class = db.Column(db.String(250), nullable=False)
    status = db.Column(db.String(250), nullable=False)
    student_type = db.Column(db.String(250), nullable=False)
    residency = db.Column(db.String(250), nullable=False)
    first_term = db.Column(db.String(250), nullable=False)
    last_term = db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True)
    first_name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    student_id = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(2500), nullable=False)
    address = db.Column(db.String(250), nullable=False)
    city = db.Column(db.String(250), nullable=False)
    state = db.Column(db.String(250), nullable=False)
    zip_code = db.Column(db.String(250), nullable=False)

    notes = db.relationship('Note')
    courses = db.relationship('Course')
    image = db.relationship('Image')
    majors = db.relationship('Major')
    GeneralInformation = db.relationship('GeneralInformation')
    

    def generate_student_id():
        # generate 8-digits long integer
        return random.randint(10000000, 99999999)
    