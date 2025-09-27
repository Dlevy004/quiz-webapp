from flask_wtf import FlaskForm
from quizapp.models import User
from wtforms import BooleanField, PasswordField, StringField, SubmitField, ValidationError


class RegistrationForm(FlaskForm):
    username = StringField()
    email = StringField()
    password = PasswordField()
    confirm_password = PasswordField()
    submit = SubmitField('Regisztráció')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('A megadott felhasználónév foglalt!')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('A megadott email foglalt!')


class LoginForm(FlaskForm):
    email = StringField()
    password = PasswordField()
    remember = BooleanField()
    submit = SubmitField('Bejelentkezés')
