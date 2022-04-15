from flask_login import LoginManager
from website import create_app
from website import views
from website import auth

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)