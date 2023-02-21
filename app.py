from flask import Flask, render_template, jsonify, url_for, flash, request, redirect, Response
import sqlite3
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

app = Flask(__name__)
app.debug=True
app.secret_key = 'MachineKey'

# a simple demo dataset will be created.
LISTEN_ALL = "0.0.0.0"
FLASK_IP = LISTEN_ALL
FLASK_PORT = 81
FLASK_DEBUG = True

login_manager = LoginManager()
login_manager.login_view = "login"

@app.route("/")
def index():
    return render_template("globalhome.html")

@app.route("/docentlogin")
def docentlogin():
    return render_template("docentlogin.html")

@app.route("/studentlogin")
def studentlogin():
    return render_template('studentlogin.html')

@app.route("/adminlogin")
def adminlogin():
    return render_template("adminlogin.html")

@app.route("/docenthome")
def docenthome():
    return render_template("docenthome.html")

@app.route("/studenthome")
def studenthome():
    return render_template("studenthome.html")

@app.route("/adminhome")
def adminhome():
    return render_template("adminhome.html")

@app.route("/api/attendance")
def list_attendance_api():
    return jsonify(
        {
            "students": [
                {"name": "Mark", "status": "aanwezig"},
                {"name": "Jane", "status": "afwezig"},
                {"name": "John", "status": "aanwezig"},
                {"name": "Henk", "status": "aanwezig"},
                {"name": "Yooo", "status": "afwezig"}
            ]
        }
    )

@app.route("/attendance")
def list_attendance():
    return render_template("attendance.html")

if __name__ == "__main__":
    app.run(host=FLASK_IP, port=FLASK_PORT, debug=FLASK_DEBUG)