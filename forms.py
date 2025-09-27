from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField


class RegistrationForm(FlaskForm):
    username = StringField()
    email = StringField()
    password = PasswordField()
    confirm_password = PasswordField()
    submit = SubmitField('Regisztráció')


class LoginForm(FlaskForm):
    email = StringField()
    password = PasswordField()
    remember = BooleanField()
    submit = SubmitField('Bejelentkezés')
