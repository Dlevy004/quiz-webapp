from flask import jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from quizapp import app, bcrypt, db
from quizapp.forms import LoginForm, RegistrationForm, UpdatePictureForm, UpdateUsernameForm
from quizapp.models import User

import os, secrets


@app.route("/")
@app.route("/index")
@login_required
def index():
    return render_template("index.html")


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


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, file_ext = os.path.splitext(form_picture.filename)
    picture_file_name = random_hex + file_ext
    picture_path = os.path.join(app.root_path ,'static/profile_pics', picture_file_name)
    form_picture.save(picture_path)
    return picture_file_name


@app.route("/profile", methods = ['GET', 'POST'])
@login_required
def profile():
    update_username_form = UpdateUsernameForm()
    update_username_form.username.data = current_user.username

    update_picture_form = UpdatePictureForm()

    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template("profile.html",
                           image_file=image_file,
                           update_username_form=update_username_form,
                           update_picture_form=update_picture_form
                           )


@app.route("/update_username", methods=["POST"])
@login_required
def update_username():
    form = UpdateUsernameForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        db.session.commit()
        return jsonify({"success": True, "message": "Profilnév sikeresen módosítva!", "new_username": current_user.username})

    errors = [err for field_errors in form.errors.values() for err in field_errors]
    return jsonify({"success": False, "message": "\n".join(errors)})


@app.route("/update_picture", methods=["POST"])
@login_required
def update_picture():
    form = UpdatePictureForm()
    if form.validate_on_submit():
        picture_file = save_picture(form.picture.data)
        current_user.image_file = picture_file
        db.session.commit()
        return jsonify({"success": True, "message": "Profilkép sikeresen módosítva!", "new_picture": current_user.image_file})

    errors = [err for field_errors in form.errors.values() for err in field_errors]
    return jsonify({"success": False, "message": "\n".join(errors)})
