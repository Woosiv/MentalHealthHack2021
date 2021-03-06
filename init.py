from flask import Flask, render_template, request
from threading import Timer
import time
import webbrowser
from flask_login import LoginManager
from exts import db
from models import User

app = Flask(__name__, static_url_path='', static_folder='static')

# Configure app
app.config.from_object('config.Config')

db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# blueprint for auth routes in the app
from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from main import main as main_blueprint
app.register_blueprint(main_blueprint)

db.create_all(app=app)

def open_browser():
    url = "http://127.0.0.1:5000/"
    webbrowser.open_new_tab(url)

if __name__ == '__main__':
    #Timer(0, open_browser).start()
    app.run(debug=True, use_reloader=False)
