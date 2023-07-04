from flask import Blueprint, render_template, redirect, request, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from .helper_db import db
import re

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')  
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        users = User.query.filter_by(email=email).all()
       
         
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.organizations'))
            else:
                flash('Incorrect password', category='error')
        else: 
            flash('Incorrect email, enter another or create an account', category='error')

    return render_template('login.html', user=current_user, users=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home')) 
 

@auth.route('/sign_up',methods=['GET','Post'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name') 
        last_name = request.form.get('last_name') 
        role = request.form.get('role')
        password_one = request.form.get('password_one')  # set initail password
        password_two = request.form.get('password_two')  # confirm password
        address = request.form.get('address')
        city = request.form.get('city')
        state = request.form.get('state')
        zip_code = request.form.get('zip_code')
        image = request.files.get('image')
         
        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists, try login!', category='error')
        elif len(email) < 4:
            flash('Incorrect email format', category='error')
        elif len(first_name) < 2:
            flash('first name too short', category='error') 
        elif password_one != password_two:  # check initial pass match confirm pass
            flash('password does not match', category='error') 
        elif len(password_one) < 8:
            flash('password must be at least 8 characters long', category='error') 
        elif not email_validator(email):
            flash('Incorrect emial format', category='error')
        elif not passwd_validator(password_one):
            flash('Incorrect password format', category='error')
        else: 
            
            filename = secure_filename(image.filename) if image else None
            image.save() if filename else None
           
            new_user = User(email=email, student_id=User.generate_student_id(),
                            first_name=first_name, last_name=last_name,
                            image=image, role=role, major=User.generate_random_major(),
                            address=address,city=city, state=state, zip_code=zip_code,
                            password=generate_password_hash(password_one, method='sha256')) 
            db.session.add(new_user)
            db.session.commit()
            
            login_user(new_user, remember=True)  # account created login user 
            flash('success', category='success') 
            return redirect(url_for('views.organizations')) 

    return render_template('sign_up.html', user=current_user)

def email_validator(email:str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.fullmatch(pattern, email):
        return True
    return False

def passwd_validator(password) -> bool:
    pattern =  r'^(?=.*[A-Z])(?!.*[:*/`~]).{8,}$'
    if re.fullmatch(pattern, password):
        return True
    return False
    