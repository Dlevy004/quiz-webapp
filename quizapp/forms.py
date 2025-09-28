from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from quizapp.models import User
from wtforms import BooleanField, PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length


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


class UpdateUsernameForm(FlaskForm):
    username = StringField(validators=[DataRequired(), Length(min=3, max=15)])
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('A megadott felhasználónév foglalt!')
    submit = SubmitField('Mentés')


class UpdatePictureForm(FlaskForm):
    picture = FileField(validators=[FileAllowed(['jpg', 'jpeg', 'png', 'webp', 'svg'])])
    submit = SubmitField('Mentés')
