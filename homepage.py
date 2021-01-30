from flask import Flask, render_template, request
from threading import Timer
import time
import webbrowser
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy
db = SQLAlchemy()

app = Flask(__name__, static_url_path='', static_folder='static')

# Configure app
app.config.from_object('config.Config')

db.init_app(app)

#Home Page
@app.route('/')
def root():
    print("sending to home")
    return app.send_static_file('home.html')

# Login Page
@app.route('/login', methods=['POST'])
def login():
    #if request.method == 'POST':
    user = request.form['username']
    password = request.form['password']
    if verifyLogin(user, password):
        print('correct user login')
        return redirect(url_for('homepage', username = user))
    else:
        print('failed login')
        return redirect(url_for('login'))
    #else:
        #return app.send_static_file('login.html')

# About
@app.route('/#')
def about():
    return render_template('about.html')

def open_browser():
    url = "http://127.0.0.1:5000/"
    webbrowser.open_new_tab(url)

if __name__ == '__main__':
    #Timer(0, open_browser).start()
    app.run(debug=True, use_reloader=False)
