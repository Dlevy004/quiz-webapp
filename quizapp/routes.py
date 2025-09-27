from flask import jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from quizapp import app, bcrypt, db
from quizapp.forms import LoginForm, RegistrationForm
from quizapp.models import User


@app.route("/")
@app.route("/auth")
def auth():
    return render_template("login.html", login_form=LoginForm(), reg_form=RegistrationForm())


@app.route("/register", methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        return jsonify({"success": True, "message": f"Sikeres regisztráció, { form.username.data }!"})
    
    errors = []
    for field, field_errors in form.errors.items():
        for err in field_errors:
            errors.append(err)
    return jsonify({"success": False, "message": "\n".join(errors)})


@app.route("/login", methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=False)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for("index"))
        return render_template("login.html", login_form=form, reg_form=RegistrationForm())
    return render_template("login.html", login_form=form, reg_form=RegistrationForm())


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('auth'))


@app.route("/index")
@login_required
def index():
    return render_template("index.html")


@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html")
