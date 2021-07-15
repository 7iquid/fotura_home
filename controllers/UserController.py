import sys
from flask import render_template, redirect, url_for, request, abort, flash, session
from flask_login import login_required, current_user
from models.User_DB import Barcode_table
from models.User_DB import User
from models.User_DB import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user


from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# def index():
#     ...

# def store():
#     ...

# def show(userId):
#     ...

# def update(userId):
#     ...

# def delete(userId):
#     ...

# def destroy(userId):sSssSssas
#     ...

def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('index'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
            
    return render_template("user_acc/login.html", user=current_user)

@login_required
def logout():
    logout_user()
    return render_template('index.html', user=None)

def sign_up():
    if request.method == 'POST':
        first_name =    request.form.get('firstName')
        position    =   request.form.get("position")
        email =         request.form.get('email')
        password1 =     request.form.get('password1')
        password2 =     request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 3:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'),position=position)
            print("actual na listahan",new_user)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            print(new_user)
            flash('Account created!', category='success')
            return render_template("index.html", user=current_user)

    return render_template("user_acc/sign_up.html", user=current_user)

@login_required
def upload_data():    
    return render_template("upload_ko.html", user=current_user)


