from flask import Flask, jsonify, render_template, url_for, flash, request, redirect, session
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from werkzeug.security import check_password_hash
import sqlite3 as sql
from datetime import datetime

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

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

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

        query = "SELECT email,password FROM studenten where email= '"+email+"' and password= '"+password+"'"
        cursor.execute(query)

        results = cursor.fetchall()

        if len(results) == 0:
            print("sorry incorrect credentials")
        else:
            if len(results) == 1:
                return render_template("studenthome.html")

    return render_template("studentlogin.html")

@app.route("/les")
def les():
    name = request.form.get('name')
    lokaal = request.form.get('lokaal')
    Date = request.form.get('Date')
    conn = sql.connect('rumble')
    c = conn.cursor()
    c.execute("INSERT INTO lessons (name, lokaal, Date) VALUES (?, ?, ?)", (name, lokaal, Date))
    conn.commit()
    conn.close()
    return render_template('les.html')
@app.route("/docenthome")
def docenthome():
    return render_template("docenthome.html")

@app.route("/studenthome", methods=['GET','POST'])
def studenthome():
    return render_template('studenthome.html')

@app.route("/adminhome")
def adminhome():
    conn = sql.connect("rumble")
    c = conn.cursor()
    c.execute("SELECT * FROM attendance")
    rows = c.fetchall()
    conn.close()
    return render_template("adminhome.html", rows=rows)

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

@app.route("/attendance", methods=["POST"])
def update_attendance():
    data = request.get_json()
    name = data['name']
    status = data['status']
    klas = data['klas']
    studentnummer = data['studentnummer']

    conn = sql.connect('rumble')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO attendance (name, date, status, klas, studentnummer) VALUES (?, ?, ?, ?, ?)", (name, formatted_datetime, status, klas, studentnummer))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Attendance updated successfully'})

@app.route('/lessons', methods=['GET'])
def get_lessons():
    conn = sql.connect('rumble')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM lessons")
    lessons = cursor.fetchall()
    conn.close()

    return jsonify(lessons)

@app.route('/add_lesson', methods=['POST'])
def add_lesson():
    data = request.get_json()
    name = data['name']

    conn = sql.connect('rumble')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO lessons (name, date) VALUES (?, date('now'))", (name,))
    lesson_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return jsonify({'message': 'Lesson added successfully', 'lesson_id': lesson_id})

@app.route('/attendance/<int:lesson_id>', methods=['GET'])
def get_attendance(lesson_id):
    conn = sql.connect('rumble')
    cursor = conn.cursor()
    cursor.execute("SELECT students.name, attendance_records.status FROM attendance_records INNER JOIN students ON attendance_records.student_id = students.id WHERE attendance_records.lesson_id = ?", (lesson_id,))
    attendance_data = cursor.fetchall()
    conn.close()

    return jsonify({'attendance_data': attendance_data})


@app.route("/qrcode")
def qrcode():
    return render_template("qrcode.html")

@app.route('/display_data')
def display_data():
    conn = sql.connect('rumble')
    cursor = conn.cursor()

    cursor.execute("SELECT les,lokaal,Date FROM lessons")
    rows = cursor.fetchall()

    conn.close()

    return render_template('les.html', rows=rows)

@app.route('/dsplay_data')
def dsplay_data():
    conn = sql.connect('rumble')
    cursor = conn.cursor()

    cursor.execute("SELECT id,name,Date FROM lessons")
    rows = cursor.fetchall()

    conn.close()

    return render_template('bijenkomst.html', rows=rows)

@app.route('/dash')
def dash():
    conn = sql.connect('rumble')
    cursor = conn.cursor()
    cursor.execute("SELECT name, studentnummer, klas, status, date FROM attendance")
    rows = cursor.fetchall()
    conn.close()
    return render_template('dash.html', rows=rows)

if __name__ == "__main__":
    app.run(host=FLASK_IP, port=FLASK_PORT, debug=FLASK_DEBUG)