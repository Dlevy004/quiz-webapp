from flask import Flask, jsonify, redirect, render_template, url_for
from forms import LoginForm, RegistrationForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'aa81185a23c8ff7da130ada119bf880a'

@app.route("/")
@app.route("/auth")
def auth():
    return render_template("login.html", login_form=LoginForm(), reg_form=RegistrationForm())


@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for("index"))
    return render_template("login.html", login_form=form, reg_form=RegistrationForm())


@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return jsonify({"success": True, "message": "Sikeres regisztráció!"})
    return jsonify({"success": False, "message": "Hiba a regisztráció során!"})


@app.route("/index")
def index():
    return render_template("index.html")