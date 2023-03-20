from flask import Flask, jsonify, render_template, url_for, flash, request, redirect, session
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user


from werkzeug.security import check_password_hash
import sqlite3 as sql

app = Flask(__name__)
app.debug = True
app.secret_key = '39201511d67c769063efb781831eac5cb95b460efbbab33a9ef9f469c13df166'

# a simple demo dataset will be created.
LISTEN_ALL = "0.0.0.0"
FLASK_IP = LISTEN_ALL
FLASK_PORT = 81
FLASK_DEBUG = True

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"




class User(UserMixin):
    def __init__(self, id, email, password):
         self.id = id
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

@login_manager.user_loader
def load_user(user_id):
    con = sql.connect("rumble")
    cur = con.cursor()
    statement = "SELECT email, password FROM user"
    cur.execute(statement)
    return User.query.get(int(user_id))

@app.route("/")
def index():
    return render_template("globalhome.html")

@app.route("/docentlogin", methods=["GET","POST"])
def docentlogin():
    if request.method == "POST":

        connection = sql.connect("rumble")
        cursor = connection.cursor()

        email = request.form["email"]
        password = request.form["password"]

        query = "SELECT email,password FROM docent where email= '"+email+"' and password= '"+password+"'"
        cursor.execute(query)

        results = cursor.fetchall()

        if len(results) == 0:
            print("sorry incorrect credentials")
        else:
            if len(results) == 1:
                return render_template("docenthome.html")

    return render_template("docentlogin.html")

@app.route("/studentlogin", methods=["GET","POST"])
def studentlogin():
    if request.method == "POST":

        connection = sql.connect("rumble")
        cursor = connection.cursor()

        email = request.form["email"]
        password = request.form["password"]

        query = "SELECT email,password FROM leerling where email= '"+email+"' and password= '"+password+"'"
        cursor.execute(query)

        results = cursor.fetchall()

        if len(results) == 0:
            print("sorry incorrect credentials")
        else:
            if len(results) == 1:
                return render_template("studenthome.html")

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

@app.route("/adminlogin", methods=["GET","POST"])
def adminlogin():
    if request.method == "POST":

        connection = sql.connect("rumble")
        cursor = connection.cursor()

        email = request.form["email"]
        password = request.form["password"]

        query = "SELECT email,password FROM user where email= '"+email+"' and password= '"+password+"'"
        cursor.execute(query)

        results = cursor.fetchall()

        if len(results) == 0:
            print("sorry incorrect credentials")
        else:
            if len(results) == 1:
                return render_template("adminhome.html")

    return render_template("adminlogin.html")

@app.route("/attendance")
def attendance():
    return render_template("attendance.html")

@app.route("/api/attendance")
def list_attendance_api():
    return jsonify(
        {
            "students": [
                {"name": "Mark", "status": "1"},
                {"name": "Jane", "status": "0"},
                {"name": "John", "status": "1"},
                {"name": "Henk", "status": "0"},
                {"name": "Karel", "status": "1"},
                {"name": "Jan", "status": "0"},
                {"name": "Ralph", "status": "1"},
                {"name": "Melanie", "status": "0"},
            ]
        }
    )
@app.route("/qrcode")
def qrcode():
    return render_template("qrcode.html")

if __name__ == "__main__":
    app.run(host=FLASK_IP, port=FLASK_PORT, debug=FLASK_DEBUG)