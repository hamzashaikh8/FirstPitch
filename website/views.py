from xml.dom.pulldom import ErrorHandler
from flask import Blueprint, appcontext_popped, render_template
from flask_login import login_user, login_required, logout_user, current_user


views = Blueprint('views', __name__)


@views.route('/')
def about():
    return render_template("about.html", user=current_user)


@views.route('/home')
@login_required
def home():
    return render_template("home.html",user=current_user)

@views.route('/profile')
@login_required
def profile():
    return render_template("profile.html",user=current_user)

@views.route('/projectpage')
@login_required
def projectpage():
    return render_template("projectpage.html",user=current_user)
