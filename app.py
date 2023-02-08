from flask import ( Flask, g , redirect, render_template, request, session, url_for, Response )

app = Flask(__name__)
app.secret_key = 'geheimekey'

# a simple demo dataset will be created.
LISTEN_ALL = "0.0.0.0"
FLASK_IP = LISTEN_ALL
FLASK_PORT = 81
FLASK_DEBUG = True

@app.route("/")
def index():
    return render_template("globalhome.html")

@app.route("/docentlogin")
def docentlogin():
    return render_template("docentlogin.html")

@app.route("/studentlogin")
def studentlogin():
    if request.method == 'POST':
        if request.form['username'] != '' or request.form[password] != '' :
            error = 'Invalid Credentials Try Again'
        else:
            return redirect(url_for('studenthome'))
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