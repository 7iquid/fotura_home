# pseudo code

import sys
from flask import render_template, redirect, url_for, request, abort
from flask_login import login_required, current_user
from models.User import Barcode_table
from models.User import User
from models.User import db

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

# def destroy(userId):
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
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("user_acc/login.html", user=current_user)

@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

def sign_up():
    if request.method == 'POST':
        email =         request.form.get('email')
        first_name =    request.form.get('firstName')
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
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("user_acc/sign_up.html", user=current_user)