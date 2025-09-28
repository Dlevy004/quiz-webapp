from quizapp import app, db
from quizapp.models_quiz import Word, Quiz, QuizItem, Attempt, Answer

# Ha True, törli a kvízhez kapcsolódó táblákat
SEED_RESET = True

EASY = [
    ("kutya", "dog"),
    ("macska", "cat"),
    ("asztal", "table"),
    ("szék", "chair"),
    ("ház", "house"),
    ("autó", "car"),
    ("alma", "apple"),
    ("könyv", "book"),
    ("toll", "pen"),
    ("ajtó", "door"),
    ("ablak", "window"),
    ("víz", "water"),
    ("kenyér", "bread"),
    ("nap", "sun"),
    ("fa", "tree"),
]

MEDIUM = [
    ("tanuló", "student"),
    ("tanár", "teacher"),
    ("város", "city"),
    ("kórház", "hospital"),
    ("repülőgép", "airplane"),
    ("kérdés", "question"),
    ("válasz", "answer"),
    ("számítógép", "computer"),
    ("egér", "mouse"),
    ("billentyűzet", "keyboard"),
    ("nyelvtan", "grammar"),
    ("fordítás", "translation"),
    ("villamos", "tram"),
    ("szótár", "dictionary"),
    ("időjárás", "weather"),
]

HARD = [
    ("meghökkentő", "astonishing"),
    ("körülményes", "cumbersome"),
    ("elméleti", "theoretical"),
    ("megkülönböztethetetlen", "indistinguishable"),
    ("végrehajthatóság", "enforceability"),
    ("következetesség", "consistency"),
    ("körforgás", "cycle"),
    ("fenntarthatóság", "sustainability"),
    ("társadalomtudomány", "social science"),
    ("földrengés", "earthquake"),
    ("vízenergia", "hydropower"),
    ("kísérletezés", "experimentation"),
    ("megvalósíthatóság", "feasibility"),
    ("valószínűségszámítás", "probability theory"),
    ("visszacsatolás", "feedback"),
]

def ensure_level_column():
    from sqlalchemy import text
    try:
        db.session.execute(text("ALTER TABLE word ADD COLUMN level VARCHAR(10) DEFAULT 'easy'"))
        db.session.commit()
        print("ℹ️  'level' oszlop hozzáadva a 'word' táblához.")
    except Exception as e:
        db.session.rollback()

def reset_quiz_tables():
    # törlések sorrendben (FK miatt)
    Answer.query.delete()
    Attempt.query.delete()
    QuizItem.query.delete()
    Quiz.query.delete()
    Word.query.delete()
    db.session.commit()
    print("🧹 Törölve: Answer, Attempt, QuizItem, Quiz, Word")

def seed_words():
    words = []
    for hu, en in EASY:
        words.append(Word(hu=hu, en=en, level="easy"))
    for hu, en in MEDIUM:
        words.append(Word(hu=hu, en=en, level="medium"))
    for hu, en in HARD:
        words.append(Word(hu=hu, en=en, level="hard"))

    db.session.add_all(words)
    db.session.commit()
    print(f"✅ Seed kész: {len(EASY)} easy, {len(MEDIUM)} medium, {len(HARD)} hard (össz: {len(words)})")

if __name__ == "__main__":
    with app.app_context():
        ensure_level_column()
        if SEED_RESET:
            reset_quiz_tables()
        seed_words()
