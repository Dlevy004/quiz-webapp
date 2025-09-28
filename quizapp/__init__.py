from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aa81185a23c8ff7da130ada119bf880a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from quizapp import models_quiz  # noqa: F401

with app.app_context():
    db.create_all()

from quizapp.routes_quiz import bp as quiz_bp
app.register_blueprint(quiz_bp)

from quizapp import routes
