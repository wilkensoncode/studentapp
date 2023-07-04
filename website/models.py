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
        return random.randint(3, 4) 


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
    student_id = db.Column(db.String(250))
    role = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(2500), nullable=False)
    address = db.Column(db.String(250), nullable=False)
    city = db.Column(db.String(250), nullable=False)
    state = db.Column(db.String(250), nullable=False)
    zip_code = db.Column(db.String(250), nullable=False)
    image = db.Column(db.String(250))
    major = db.Column(db.String(250))

    # user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 

    notes = db.relationship('Note')
    courses = db.relationship('Course')  
    GeneralInformation = db.relationship('GeneralInformation')
    

    def __init__(self, email, first_name, last_name, student_id, major, role, password, address, city, state, zip_code, image=None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.role = role
        self.password = password
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.image = image
        self.major = major

    @staticmethod
    def generate_student_id():
        # generate 8-digit long integer
        return str(random.randint(10000000, 99999999))

    @staticmethod
    def generate_random_major():
        majors_degrees = [
            "Accounting",
            "Aerospace Engineering",
            "Anthropology",
            "Architecture",
            "Art History",
            "Biology",
            "Business Administration",
            "Chemical Engineering",
            "Chemistry",
            "Civil Engineering",
            "Communications",
            "Computer Science",
            "Criminal Justice",
            "Economics",
            "Education",
            "Electrical Engineering",
            "English Literature",
            "Environmental Science",
            "Finance",
            "Graphic Design",
            "History",
            "Human Resources",
            "Information Technology",
            "International Relations",
            "Journalism",
            "Marketing",
            "Mathematics",
            "Mechanical Engineering",
            "Music",
            "Nursing",
            "Philosophy",
            "Physics",
            "Political Science",
            "Psychology",
            "Sociology",
            "Theater Arts",
            "Veterinary Medicine"
        ]
        return random.choice(majors_degrees)
    
 

   
