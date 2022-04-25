from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    data = request.form 
    print(data)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print('email is: ',email)
        print('password is: ',password)
        user = User.query.filter_by(email=email).first()
        if user:
            print(password)
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/projectpage', methods=['GET','POST'])
@login_required
def projectpage():
    if request.method=='POST':
        flash('Thank you for submitting an offer!', category='success')
    return render_template("projectpage.html",user=current_user)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    data=request.form 
    print(data)

    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstname')
        last_name = request.form.get('lastname')
        password1 = request.form.get('password')
        password2 = request.form.get('password2')
        role = request.form.get('role')

        print('email is : ',email,type(email))
        print('firstname is : ',first_name,type(first_name))
        print('lastname is : ',last_name,type(last_name))
        print('password1 is : ',password1,type(password1))
        print('password2 is : ',password2,type(password2))
        print('role is : ',role,type(role))


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
            new_user = User(email=email, first_name=first_name, last_name=last_name, password=generate_password_hash(
                password1, method='sha256'),role=role)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)