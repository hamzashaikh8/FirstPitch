from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'U8MYFIRSTPITCHHEHE'
    return app