from flask import Blueprint, render_template, request, flash, jsonify,current_app
from flask_login import login_required, current_user
import json 
import os 
from .models import *
from .helper_db import db



views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST']) 
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id) 
            db.session.add(new_note)
            db.session.commit()
            flash('Note added', category='success')
    # getting relative path to json file
    from app import create_app 
    app = create_app()
    static_folder = app.static_folder
    current_directory = os.getcwd()  
    json_path = os.path.join(current_directory, static_folder, 'js', 'school.json')
    
    with open(json_path) as json_file:
        school = json.load(json_file) 

    return render_template('index.html', user=current_user, school=school, zip=zip)

@views.route('/delete_note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    print(note)
    noteId = note['noteId']
    print(noteId)
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})

@views.route('/courses', methods=['GET', 'POST'])
@login_required
def courses():
    if request.method == 'POST':
        course_title = request.form.get('course_title') 
        if len(course_title) < 3:
            flash('Needs to be at leat 3 letters long (SCI or Science)', category='error')
        else:
            new_course = Course(course_title=course_title,course_number=Course.generate_course_number(), credit=Course.genrate_course_credit(),  user_id=current_user.id)
            db.session.add(new_course)
            db.session.commit()
            flash('Course added!', category='cuccsess')

    return render_template('course.html', user=current_user)

@views.route('/profile')
@login_required
def profile():
    # if request.method == 'POST':
    #     student_class = request.form.get("student_class")
    #     status = request.form.get("status")
    #     student_type = request.form.get("student_type")
    #     residency = request.form.get("residency")
    #     first_term = request.form.get("first_term")
    #     last_term = request.form.get("last_term")
    #     user_id = request.form.get("user_id")

    #     generalInformation = (
    #         GeneralInformation(status=GeneralInformation.status())
            
    #                                             )


    return render_template('profile.html', user=current_user)