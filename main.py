from flask import render_template
from flask_login import LoginManager, current_user
from website import create_app
from website import views
from website import auth

app = create_app()

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", user=current_user), 404

if __name__ == '__main__':
    app.run(debug=True)