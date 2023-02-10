from flask import Flask
from flask import render_template, url_for, flash, request, redirect, Response
import sqlite3
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

app = Flask(__name__)
app.debug=True
app.secret_key = 'geheimekey'

# a simple demo dataset will be created.
LISTEN_ALL = "0.0.0.0"
FLASK_IP = LISTEN_ALL
FLASK_PORT = 81
FLASK_DEBUG = True

login_manager = LoginManager(app)
login_manager.login_view = "login"
class User(UserMixin):
    def __init__(self, id, email, password):
         self.id = unicode(id)
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
   conn = sqlite3.connect('/var/www/flask/login.db')
   curs = conn.cursor()
   curs.execute("SELECT * from login where id = (?)",[user_id])
   lu = curs.fetchone()
   if lu is None:
      return None
   else:
      return User(int(lu[0]), lu[1], lu[2])
@app.route("/login", methods=['GET','POST'])
def login():
  if current_user.is_authenticated:
     return redirect(url_for('profile'))
  form = LoginForm()
  if form.validate_on_submit():
     conn = sqlite3.connect('/var/www/flask/login.db')
     curs = conn.cursor()
     curs.execute("SELECT * FROM login where email = (?)",    [form.email.data])
     user = list(curs.fetchone())
     Us = load_user(user[0])
     if form.email.data == Us.email and form.password.data == Us.password:
        login_user(Us, remember=form.remember.data)
        Umail = list({form.email.data})[0].split('@')[0]
        flash('Logged in successfully '+Umail)
        redirect(url_for('profile'))
     else:
        flash('Login Unsuccessfull.')
  return render_template('studentlogin.html',title='Login', form=form)
if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8080,threaded=True)

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

if __name__ == "__main__":
    app.run(host=FLASK_IP, port=FLASK_PORT, debug=FLASK_DEBUG)