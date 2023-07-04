from flask import Flask 
from os import path
from .models import *  # load models
from .helper_db import db
from flask_login import LoginManager
 
from dotenv import load_dotenv
import os

from .views import views 
from .auth import auth 

DB_NAME = "student"

def create_app():
    load_dotenv()
    app = Flask(__name__) 
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') 
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
    db.init_app(app)
   
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    with app.app_context():
        create_database() 
     
    loggin_manager = LoginManager()
    loggin_manager.login_view = 'auth.login'
    loggin_manager.init_app(app)
    @loggin_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
        
    return app

def create_database():
    if not path.exists('website/' + DB_NAME): 
        db.create_all()
        print('Created db!')


