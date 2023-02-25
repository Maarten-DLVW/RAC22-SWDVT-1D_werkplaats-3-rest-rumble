from flask import Flask
from flask import render_template, url_for, flash, request, redirect, Response
import sqlite3
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user


app = Flask(__name__)
app.debug=True
app.secret_key = '39201511d67c769063efb781831eac5cb95b460efbbab33a9ef9f469c13df166'

# a simple demo dataset will be created.
LISTEN_ALL = "0.0.0.0"
FLASK_IP = LISTEN_ALL
FLASK_PORT = 81
FLASK_DEBUG = True

login_manager = LoginManager(app)
login_manager.login_view = "login"

class User(UserMixin):
    def __init__(self, id, email, password):
         self.id = (id)
         self.email = email
         self.password = password
         self.authenticated = False
    def is_active(self):
         return self.is_active()
    def is_anonymous(self):
         return False
    def is_authenticated(self):
         return self.authenticated
    def is_active(self):
         return True
    def get_id(self):
         return self.id

db = sqlite3
@login_manager.user_loader
def load_user(user_id):
        return User(int(user_id))

@app.route("/")
def index():
    return render_template("globalhome.html")

@app.route("/docentlogin")
def docentlogin():
    return render_template("docentlogin.html")

@app.route("/studentlogin")
def studentlogin():
    return render_template("studentlogin.html")
@app.route("/nav")
def nav():
    return render_template("nav.html")

@app.route("/docenthome")
def docenthome():
    return render_template("docenthome.html")

@app.route("/studenthome")
def studenthome():
    return render_template("studenthome.html")

@app.route("/adminhome")
def adminhome():
    return render_template("adminhome.html")

@app.route("/adminlogin")
def adminlogin():
    return render_template("adminlogin.html")


if __name__ == "__main__":
    app.run(host=FLASK_IP, port=FLASK_PORT, debug=FLASK_DEBUG)