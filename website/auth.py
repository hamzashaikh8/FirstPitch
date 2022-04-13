from flask import Blueprint, Flask, render_template, request

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    data = request.form 
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    data = request.form 
    print(data)
    return render_template("sign_up.html")