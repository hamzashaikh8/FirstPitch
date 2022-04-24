from flask import Blueprint, render_template
from flask_login import login_user, login_required, logout_user, current_user


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", user=current_user)

@views.route('/profile')
def profile():
    return render_template("profile.html")

