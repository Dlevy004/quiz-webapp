import uuid
from datetime import datetime
from quizapp import db  # a db példány az __init__.py-ból jön

def gen_uuid() -> str:
    return str(uuid.uuid4())

class Word(db.Model):
    __tablename__ = 'word'
    id = db.Column(db.Integer, primary_key=True)
    hu = db.Column(db.Text, nullable=False)   # magyar szó
    en = db.Column(db.Text, nullable=False)   # angol szó
    part_of_speech = db.Column(db.String(32)) # opcionális (ige, főnév stb.)
    tags = db.Column(db.Text)                 # pl: "A1,food"
    level = db.Column(db.String(10), nullable=False, default="easy")

    def __repr__(self):
        return f"<Word {self.hu} - {self.en}>"

class Quiz(db.Model):
    __tablename__ = 'quiz'
    id = db.Column(db.String(36), primary_key=True, default=gen_uuid)
    direction = db.Column(db.String(10), nullable=False)  # 'HU_EN' | 'EN_HU'
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class QuizItem(db.Model):
    __tablename__ = 'quiz_item'
    id = db.Column(db.String(36), primary_key=True, default=gen_uuid)
    quiz_id = db.Column(db.String(36), db.ForeignKey('quiz.id', ondelete='CASCADE'))
    word_id = db.Column(db.Integer, db.ForeignKey('word.id'))
    prompt = db.Column(db.Text, nullable=False)
    correct_index = db.Column(db.Integer, nullable=False)
    choices_json = db.Column(db.Text, nullable=False)  # a 4 válasz JSON-ben

class Attempt(db.Model):
    __tablename__ = 'attempt'
    id = db.Column(db.String(36), primary_key=True, default=gen_uuid)
    quiz_id = db.Column(db.String(36), db.ForeignKey('quiz.id'))
    user_id = db.Column(db.String(64))  # opcionális: Flask-Login user id
    started_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    finished_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    score = db.Column(db.Integer, nullable=False)
    correct_count = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)

class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.String(36), primary_key=True, default=gen_uuid)
    attempt_id = db.Column(db.String(36), db.ForeignKey('attempt.id', ondelete='CASCADE'))
    item_id = db.Column(db.String(36), db.ForeignKey('quiz_item.id'))
    chosen_index = db.Column(db.Integer, nullable=False)
    time_ms = db.Column(db.Integer, nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)
